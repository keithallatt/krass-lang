import sys

# sys.argv should = [script name, raw file, compiled file]
if len(sys.argv) != 3:
	# this should never happen, because this is called from a shell script. 
	# If it does, theres an issue passing files along between Shell and Python

	exit(1)

raw_file = sys.argv[1]
compiled_file = sys.argv[2]



