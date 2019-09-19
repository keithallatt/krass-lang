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

# Get file extension
ext="${FILE#*.}"

# make extension lowercase.
ext=$(echo "$ext" | tr '[:upper:]' '[:lower:]')


if [ "${ext}" != "krass" ]; then
	echo "Cannot compile non-Krass file. Please ensure file extension is *.krass";
	exit 1
fi

# create blank TeX file with "tex" file extension appended to the name (i.e. *.krass -> *.tex)

COMPILED="${FILE%%.*}"
PDF_FILE=$COMPILED
PDF_FILE+=".pdf"
COMPILED+=".tex"
touch $COMPILED

# Parse through file
# extract Krass components
# pass Krass components to krass2python.py
python3 parseKrass.py $FILE $COMPILED

pdflatex -halt-on-error $COMPILED | grep '^!.*' -A200 --color=always 

# can change later if you want, by default, open the pdf after generation.

open $PDF_FILE

