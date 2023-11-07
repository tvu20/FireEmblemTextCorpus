# this file strips quotes.txt of all quotation marks and places the output in output.txt.

import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "linebreaks.txt"), 'r') as f, open(os.path.join(__location__, "quotes.txt"), 'w') as fo:
    for line in f:
        fo.write(line)
        fo.write("\n")
        # nextline = next(f, None)
        # nextline = next(f, None)
        # print("next line", nextline)
   
        # SERENES FOREST!!!!!!!!
        # nextline = next(f, None)

        # if nextline is None:
        #     continue

        # if len(nextline.strip()) == 0:
        #     fo.write("\n")
        #     continue


        # newline = line.strip() + " " + nextline.strip() + "\n"
        # fo.write(newline)
        # nextline = next(f, None)
        # END SERENES FOREST!!!!!!

        # fo.write(line + "\n")