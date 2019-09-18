import sys
import tempfile
import re
import subprocess


def compile_krass_conditional(krass_conditional):
	"""
	Compile Krass conditional statements to Python conditional statements.
	"""
	# change true to True, && to and etc.
	changes = [
		("true", "True"),
		("false", "False"),
		("&&", " and "),
		("||", " or "),  # keep an eye on this one, for regex or non
		("!", " not ")
	]

	for change in changes:
		krass_conditional = krass_conditional.replace(change[0], change[1])	

	return krass_conditional


def compile_krass(krass_file_contents):
	"""
	Compile a section of krass code. 
	For any boolean operation not in a if/else if/while, 
	Python formatting is required (as of now)
	"""
	tf = tempfile.NamedTemporaryFile(delete=False)
		
	original_path = tf.name
	
	# generate python file. writing to `tf`
	
	# since Krass needs proper formatting, line by line execution should be ok.
	# 	if a line fits a special requirement, such as imports, function declarations, 
	# 	if statements or loops, appropriate action will take place. Indent level will be
	#	controlled by curly braces ( '{' and '}' ), in the case of blocks of code. Indentation
	#	in Krass code doesn't matter, so it will be stripped off, and added in post translation

	# 	Failure to format code properly will lead to broken Python translations, 
	
	indent_level = 0
	
	struct_mode = False  # if defining a struct
	
	for line in krass_file_contents.split("\n"):
		line = line.strip()  # remove whitespace
		output_line = "\t" * indent_level

		if struct_mode:
			if line == "}":
				struct_mode = False
				indent_level -= 2
			if "=" in line:
				# default value
				output_line += line.replace(";", "")  # remove the ; if it was added.
			else:
				# no default value
				output_line += line.replace(";", "") + " = None"

			output_line += "\n"
			tf.write(bytes(output_line, 'utf-8'))
			continue

		special_line = False

		# check for function block
		z = re.match("function\\s+(\\w+)\\(((\\w+){0,1}|((\\w+,\\s*)+(\\w+)))\\)\\s*\\{", line)
		if z:
			special_line = True
			# create function declaration.
			# isolate function signature
			function_signature = line[8:-1].strip() 
			output_line += "def " + function_signature + ":"
			indent_level += 1
				
		# If blocks
		z = re.match("if\\s*\\((.*)\\)\\s*{", line)
		if z:
			special_line = True
			# create if block declaration
			conditional = z.group(1) 
			output_line += "if " + compile_krass_conditional(conditional) + ":"						
			indent_level += 1

		# Else if blocks
		z = re.match("}\\s*else\\s+if\\s*\\((.*)\\)\\s*{", line)
		if z:
			special_line = True			
			conditional = z.group(1)
			# remove a tab and add in the elif block, don't change indentation.
			output_line = output_line[:-1] + "elif " + compile_krass_conditional(conditional) + ":"
		
		# Else blocks
		z = re.match("}\\s*else\\s*{", line)
		if z:
			special_line = True
			output_line = output_line[:-1] + "else:"		

		# For Loops
		z = re.match("for\\s*\\((.*)\\s*:\\s*(.*)\\)\\s*{", line)
		if z:
			special_line = True
			item = z.group(1)
			iterator = z.group(2)
			output_line += "for " + item + " in " + iterator + ":"
			indent_level += 1

		# While Loops
		z = re.match("while\\s*\\((.*)\\)\\s*{", line)
		if z:
			special_line = True
			conditional = z.group(1)
			output_line += "while " + compile_krass_conditional(conditional) + ":"
			indent_level += 1

		# structs
		z = re.match("struct\\s+(.*)\\s*{", line)
		if z:
			special_line = True
			name = z.group(1)
			output_line += "class "+name+":\n\t"+("\t"*indent_level)+"def __init__(self):"
			struct_mode = True
			indent_level += 2
		
		# End of blocks: i.e. '}' as a line.
		z = re.match("}", line)
		if z:
			special_line = True
			indent_level -= 1	
			
		# for now, no exception handling will be implementable. 

		# not a special line, so treat it as pure python.
		if not special_line:
			output_line += line.replace(";", "")

		output_line += "\n"
		tf.write(bytes(output_line, 'utf-8'))

	# file needs to be closed first.
	tf.close()
	# create a subprocess with file generated
	
	cmd = subprocess.run(["python3", original_path], stdout=subprocess.PIPE)
	stdout = cmd.stdout.decode()  # bytes => str
	
	return stdout


# sys.argv should = [script name, raw file, compiled file]
if len(sys.argv) != 3:
	# this should never happen, because this is called from a shell script. 
	# If it does, theres an issue passing files along between Shell and Python

	exit(1)

raw_file = sys.argv[1]
compiled_file = sys.argv[2]

compiled_file = open(compiled_file, 'w')

contents = open(raw_file, 'r').read()

for chunk in contents.split("?::"):
	if "::?" in chunk:
		# contains a krass chunk
		tex_chunk, krass_chunk = chunk.split("::?")[0], chunk.split("::?")[1]
		
		compiled_file.write(tex_chunk)
		compiled_file.write(compile_krass(krass_chunk))

	else:
		# probably end, no krass chunk, or malformed. 
		compiled_file.write(chunk)


