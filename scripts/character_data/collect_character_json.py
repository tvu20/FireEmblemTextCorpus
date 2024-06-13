import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file_content = []

with open(os.path.join(__location__, "char_table.txt"), 'r') as pcs:
    for line in pcs:
        splits = line.strip().split(",")

        file_content.append({"name": splits[0], "class": splits[1], "appears": splits[2], "joins": splits[3], "img": splits[6]})


with open(os.path.join(__location__, "char_data.json"), 'w') as fo:
    json.dump(file_content, fo)