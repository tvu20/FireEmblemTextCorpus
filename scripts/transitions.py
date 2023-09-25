import os
import json
import csv
import glob
import sys

path_to = os.path.join(os.getcwd(), "data", sys.argv[1])
path_from = os.path.join(path_to, "chapters")

genders = {
    "M": "male",
    "F": "female",
    "N": "neutral",
    "A": "avatar",
    "-": "-"
}

file_content = {}

# reading JSON
for filename in glob.glob(os.path.join(path_from, "*.json")):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        data = json.load(f)

        transitions = data["transitions"]

        for i in range(len(transitions) - 1):
            pairing = transitions[i] + transitions[i+1]

            if pairing not in file_content:
                file_content[pairing] = 1
            else:
                file_content[pairing] += 1

file_content = dict(sorted(file_content.items(), key=lambda x:x[1], reverse=True))

with open(os.path.join(os.getcwd(), path_to, "transitions.csv"), 'w') as file:
    writer = csv.writer(file)
    field = ["pairing", "from", "to", "frequency"]
    writer.writerow(field)

    for pairing in file_content:
        from_ = genders[pairing[0]]
        to_ = genders[pairing[1]]
        
        writer.writerow([pairing, from_, to_, file_content[pairing]])

