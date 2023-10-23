# this file strips quotes.txt of all quotation marks and places the output in output.txt.

import os
import re 

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "parentheses.txt"), 'r') as f, open(os.path.join(__location__, "linebreaks.txt"), 'w') as fo:
    for line in f:
        text = line.strip()

        # remove lines that are just parentheses
        if len(text) > 0 and text[0] == "(" and text[-1] == ")":
            # fo.write("")
            # fo.write("")
            fo.write("\n\n")
            # nextline = next(f, None)

            # if len(nextline.strip()) != 0:
            #     fo.write(nextline)
            continue 

        # remove in-line parentheses
        else:
            new_text = line.replace("(Name of tactician)", "Mark")
            new_text = re.sub(r'\([^)]*\)', '', new_text)
            new_text = new_text.replace(" :", ":")

            # this is just for fe7! will remove later
            new_text = new_text.replace("In-game message", "Tutorial")

            fo.write(new_text)