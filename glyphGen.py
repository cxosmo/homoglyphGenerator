#!/usr/bin/env python3

import homoglyphs as hg
import sys

if len(sys.argv) < 2:
    print("Please pass a string/domain/username/whatever as input (e.g. ./glyphs.py john.smith@example.com)") 
    sys.exit()

# Load all languages 
hg.Homoglyphs(languages={'cz', 'et', 'sk', 'bg', 'hu', 'en', 'es', 'be', 'vi', 'hr', 'de', 'lt', 'ru', 'fi', 'th', 'nl', 'pt', 'eo', 'da', 'ca', 'pl', 'tr', 'el', 'mk', 'he', 'ar', 'lv', 'sr', 'sl', 'it', 'fr', 'ro'})

def homoglyph_generator(stringInput):
    if "@" in stringInput:
        tld = stringInput[stringInput.rindex('.'):]
        stringInput = stringInput[:stringInput.rindex('.')]
    else:
        tld = ""
    myInput = list(stringInput)
    counter = 0
    for letter in myInput:
        glyphList = hg.Homoglyphs().get_combinations(letter)
        for glyph in glyphList:
            myInput[counter] = glyph
            print(''.join(myInput) + tld + " --- The letter " + letter + " was replaced with " + glyph)
            myInput[counter] = letter
        counter += 1

homoglyph_generator(sys.argv[1])
