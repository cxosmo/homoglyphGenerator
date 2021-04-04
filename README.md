# homoglyph_generator
A Python script that takes a string as input and outputs available character-by-character homoglyph permutations of it. 

_Printing of Unicode characters can be handled inconsistently depending on environmental factors (i.e. operating system/locale settings). Use the _`--verbose`_ flag to include raw Unicode of the substituted character._ 

## Usage
```
usage: homoglyph_generator.py [-h] -i INPUT [-v]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        (required) specify a string or file as input
  -v, --verbose         verbose output includes referencing of substituted
                        character, substituting character and UTF-8 code
```

