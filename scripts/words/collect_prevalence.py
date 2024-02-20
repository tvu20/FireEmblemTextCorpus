# this file generates a list of links based on character pairing matrix. places output in links.json

import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file_content = []

with open(os.path.join(__location__, "prevalence.txt"), 'r') as f, open(os.path.join(__location__, "All.json"), 'w') as fo:
    for line in f:
        line = line.strip()
        splits = line.split(',')



        if any(char.isdigit() for char in splits[0]):
            continue

        if (splits[1] == "occurrence"):
            continue

        file_content.append({"word": splits[0], "occurrence": float(splits[1]), "set": "All"})

    json.dump(file_content, fo)