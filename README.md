# Krass

Krass Programming language. Krass is designed to integrate into TeX documents to be more computably functional. Much like PHP adds to HTML code, Krass adds to TeX. 

Technically, TeX is Turing complete, but defining functions can be extremely difficult when they don't revolve around typesetting. Krass is designed to take file input and compute results to be typeset by TeX. The resulting plain TeX file is also kept to view results in TeX. 

## Setup

To set up krass, first download the repository, and run `setup.sh`. This will move the files to a hidden directory (on Mac and Linux). To use Krass in Atom, which is heavily recommended, use the package `process-palette` and create a custom process. Under "Shell Command:", type `~/.krass-lang/krassc.sh {fileDirAbsPath}/*.krass`.

If you prefer other text editors, you can use the command line to compile files, using `> ~/.krass-lang/krassc.sh {file}`.

