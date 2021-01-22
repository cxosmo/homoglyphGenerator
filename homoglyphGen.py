#!/usr/bin/env python3

import sys,argparse
import homoglyphs as hg

def homoglyph_generator(stringInput):
    hg.Homoglyphs(languages={'cz', 'et', 'sk', 'bg', 'hu', 'en', 'es', 'be', 'vi', 'hr', 'de', 'lt', 'ru', 'fi', 'th', 'nl', 'pt', 'eo', \
         'da', 'ca', 'pl', 'tr', 'el', 'mk', 'he', 'ar', 'lv', 'sr', 'sl', 'it', 'fr', 'ro'})
    
    # Basic logic for checking if email passed as input in order to exclude TLDs from homoglyph swapping
    if "@" in stringInput:
        tld = stringInput[stringInput.rindex('.'):]
        stringInput = stringInput[:stringInput.rindex('.')]
    else:
        tld = ""
    myInput = list(stringInput)
    counter = 0

    # Loop through user input, performing single-character swaps against each letter with associated homoglyphs
    for letter in myInput:
        glyphList = hg.Homoglyphs().get_combinations(letter)
        for glyph in glyphList:

            # Replace letter in user's input with homoglyph
            myInput[counter] = glyph
            if args.verbose:

                # Starting item in each letter's homoglyph list is its original ascii representation, hence skip verbose strings
                if glyphList.index(glyph) == 0:
                    print(''.join(myInput) + tld + " --- No replacements made.")
                
                # Print user's input + TLD (if inputted), along with verbose info + bytecode of swapped homoglyph
                else:
                    print(''.join(myInput) + tld + " --- The letter " + letter + " was replaced with " + glyph \
                    + ". (Bytecode: " + str(glyph.encode('utf-8')).replace("'","").replace("b","",1) + ")")
            else:
                print(''.join(myInput) + tld)
            
            # Reset user input to pre-swapped state to avoid more than one homoglyph in output
            myInput[counter] = letter
        counter += 1

if __name__ == "__main__":
    # Parse command line
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input",
                        help="(required) specify a string as input (e.g. 'john.smith@example.com')",
                        required="True", action="store")
    parser.add_argument("-v", "--verbose",
                        help="verbose output includes referencing of substituted character, substituting \
                              character and UTF-8 code.",
                        action="store_true")
    args = parser.parse_args()

homoglyph_generator(args.input)
