# this file strips quotes.txt of all quotation marks and places the output in output.txt.

import os
import re 

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "brackets.txt"), 'r') as f, open(os.path.join(__location__, "output.txt"), 'w') as fo:
    for line in f:
        text = line.strip()

        while True:
            nextline = next(f, None)
            if nextline is None or nextline.strip() == "":
                break
            else:
                text += " " + nextline.strip()

        if text == "-------------------------------------------------------------------------------":
            fo.write("\n")
            continue

        # remove lines that are just parentheses
        if len(text) > 0 and text[0] == "[" and text[-1] == "]":
            # fo.write("")
            # fo.write("")
            # fo.write("\n\n")
            fo.write("\n")
            # nextline = next(f, None)

            # if len(nextline.strip()) != 0:
            #     fo.write(nextline)
            continue 

        # remove in-line parentheses
        else:
            # new_text = re.sub(r'\([^)]*\)', '', new_text)
            next_text = re.sub(r"([\(\[]).*?([\)\]])", '', text)

            # next_text = text.replace("(", "")
            # next_text = next_text.replace(")", "")
            # next_text = next_text.replace(" ???", "")

            fo.write(next_text + "\n")