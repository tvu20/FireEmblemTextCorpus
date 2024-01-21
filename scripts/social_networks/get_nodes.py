# this file generates a list of nodes based on character names. places output in nodes.json

import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file_content = {}
file_content["nodes"] = []

with open(os.path.join(__location__, "names.txt"), 'r') as f, open(os.path.join(__location__, "genders.json"), 'r') as fg, open(os.path.join(__location__, "nodes.json"), 'w') as fo:
    genders = json.load(fg)

    for line in f:
        name = line.strip()

        gender = genders[name]


        file_content["nodes"].append({"id": name, "gender": gender})
    
    json.dump(file_content, fo)
