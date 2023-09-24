import os
import re
import json
import glob
import sys

path_from = sys.argv[1]
path_to = sys.argv[2]

tags = ["intro", "battle", "end", "visit", "flashback", "recruit-visit", "recruit-battle", "character-falls", "dialogue", "boss", "recruit-talk", "battle-talk"]

gender_info = {}

file_content = {}
file_content["descriptions"] = []
file_content["counts"] = {}

with open(os.path.join(os.getcwd(), path_to, "genders.json"), 'r') as f:
    gender_info = json.load(f)

# reading JSON
for filename in glob.glob(os.path.join(path_from, "*.json")):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        data = json.load(f)

        for person in data["speakers"]:
            if person not in file_content["counts"]:
                file_content["descriptions"].append({"name": person, "gender": gender_info[person]})
                file_content["counts"][person] = data["dialogue_counts"][person]
            else:
                file_content["counts"][person] += data["dialogue_counts"][person]

# sorting and writing speaker counts
with open(os.path.join(os.getcwd(), path_to, "speakers.json"), 'w') as file:
    sorted_counts = sorted(file_content["counts"].items(), key=lambda x:x[1], reverse=True)

    file_content["counts"] = dict(sorted_counts)
    json.dump(file_content, file)

