#!/bin/bash
# Krass Compiler Shell Script:
#     Takes care of passing file contents to a compiler written in a 
#     different language. After it is all parsed through into pure TeX, 
#     the resultant TeX file will be passed through a TeX compiler and
#     the final PDF file will be kept.

# input is a Krass file. extension-> *.krass
FILE=""

if (($# == 1)); then
	FILE=$1
else
	echo "Wrong number of arguments. Only supply parent directory."
	exit 1
fi

ext="${FILE#*.}"

ext=$(echo "$ext" | tr '[:upper:]' '[:lower:]')


if [ "${ext}" == "krass" ]; then
	echo "Parsing $FILE"
else
	echo "Cannot compile non-Krass file. Please ensure file extension is *.krass";
fi

# create blank TeX file with "_compiled" appended to the name (i.e. *.krass -> *_compiled.tex)


# Parse through file


# extract Krass components


# pass Krass components to krass2python.py


# use generated file to append to running total of TeX code
# python3 *_python.py >> *_compiled.tex





