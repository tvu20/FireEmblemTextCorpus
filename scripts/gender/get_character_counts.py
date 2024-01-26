 #this file generates a list of line counts for each gender speaking per game

import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file_content = {}
file_content["pcs"] = set()
file_content["npcs"] = set()
file_content["pcCounts"] = {}
file_content["npcCounts"] = {}
file_content["counts"] = {}

genders = {}

with open(os.path.join(__location__, "genders.json"), 'r') as f:
    genders = json.load(f)

with open(os.path.join(__location__, "pc_names.txt"), 'r') as pcs:
    for line in pcs:
        name = line.strip()
        # gender = genders[name]
        # delete this!
        if name not in genders:
            print(name)
            gender = "M"
        else:
            gender = genders[name]

        file_content["pcs"].add(name)

        if gender not in file_content["pcCounts"]:
            file_content["pcCounts"][gender] = 0

        file_content["pcCounts"][gender] += 1

with open(os.path.join(__location__, "npc_names.txt"), 'r') as npcs:
    for line in npcs:
        name = line.strip()

        # delete this!
        if name not in genders:
            print(name)
            gender = "M"
        else:
            gender = genders[name]

        file_content["npcs"].add(name)

        if gender not in file_content["npcCounts"]:
            file_content["npcCounts"][gender] = 0

        file_content["npcCounts"][gender] += 1

with open(os.path.join(__location__, "character_counts.json"), 'w') as fo:
    file_content["pcs"] = list(file_content["pcs"])
    file_content["npcs"] = list(file_content["npcs"])

    gender_tags = ["M", "F", "N", "A"]

    for gender_tag in gender_tags:
        if gender_tag in file_content["npcCounts"] and gender_tag in file_content["pcCounts"]:
            file_content["counts"][gender_tag] = file_content["pcCounts"][gender_tag] + file_content["npcCounts"][gender_tag]
        elif gender_tag in file_content["pcCounts"]:
            file_content["counts"][gender_tag] = file_content["pcCounts"][gender_tag]
        elif gender_tag in file_content["npcCounts"]:
            file_content["counts"][gender_tag] = file_content["npcCounts"][gender_tag]

    json.dump(file_content, fo)