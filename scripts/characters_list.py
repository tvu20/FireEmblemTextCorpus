import os
import re
import json
import glob
import sys

path_to = os.path.join(os.getcwd(), "input", sys.argv[1])
path_from = os.path.join(path_to, "chapters")

output_path = os.path.join(os.getcwd(), "data", sys.argv[1])
input_path = os.path.join(output_path, "chapters")

tags = ["intro", "battle", "end", "visit", "flashback", "recruit-visit", "recruit-battle", "character-falls", "dialogue", "boss", "recruit-talk", "battle-talk"]

gender_info = {}

file_content = {}
file_content["descriptions"] = []
file_content["counts"] = {}

print("Running character list on " + sys.argv[1])

with open(os.path.join(os.getcwd(), path_to, "genders.json"), 'r') as f:
    gender_info = json.load(f)

# reading JSON
for filename in glob.glob(os.path.join(input_path, "*.json")):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        data = json.load(f)

        for person in data["speakers"]:
            if person not in file_content["counts"]:
                gender = ''
                if person in gender_info:
                    gender = gender_info[person]

                file_content["descriptions"].append({"name": person, "gender": gender})
                file_content["counts"][person] = data["dialogue_counts"][person]
            else:
                file_content["counts"][person] += data["dialogue_counts"][person]

# sorting and writing speaker counts
with open(os.path.join(os.getcwd(), output_path, "speakers.json"), 'w') as file:
    sorted_counts = sorted(file_content["counts"].items(), key=lambda x:x[1], reverse=True)

    file_content["counts"] = dict(sorted_counts)
    json.dump(file_content, file)

