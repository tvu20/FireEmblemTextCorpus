# this file strips quotes.txt of all quotation marks and places the output in output.txt.

import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "quotes.txt"), 'r') as f, open(os.path.join(__location__, "output.txt"), 'w') as fo:
    for line in f:
        line = line.replace('"', '').replace('“', '').replace('”', '')
        line = line.replace('…', '...')

        split_string = line.split(':')
        # print(split_string[1])
        if len(split_string) > 1 and split_string[1][0] != " ":
            split_string[1] = " " + split_string[1]

        fo.write(':'.join(split_string))
        # fo.write(line.replace('"', '').replace('“', '').replace('”', ''))