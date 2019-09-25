#!/bin/bash

# create the krass lang directory
mkdir ~/.krass-lang

# copy all files over.
cp -r ./* ~/.krass-lang/

bp=$(<~/.bash_profile)

if [[ $bp != *"alias krassc"* ]]; then 
	
	echo "alias krassc='~/.krass-lang/krassc.sh'" >> ~/.bash_profile
		
	source ~/.bash_profile

	echo "Alias krass now exists";
else
	echo "Alias krassc already exists";
fi


echo "Setup complete."
