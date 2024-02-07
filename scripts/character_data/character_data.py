import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file_content = []

with open(os.path.join(__location__, "gender.json"), 'r') as f:
    genders = json.load(f)

with open(os.path.join(__location__, "chars.txt"), 'r') as pcs:
    for line in pcs:
        splits = line.split("	")

        if splits[0] not in genders:
            print(splits[0])
            continue

        file_content.append({"name": splits[0], "gender": genders[splits[0]], "class": splits[1].strip() })

with open(os.path.join(__location__, "output.json"), 'w') as fo:
    json.dump(file_content, fo)