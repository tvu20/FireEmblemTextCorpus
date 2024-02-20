import os
import csv
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

data = []

with open(os.path.join(__location__, "data.csv"), 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)

# print(data[:10])

file_content = {}

for row in data[1:]:
    chapter = row[1]
    label = row[4]

    if chapter not in file_content:
        file_content[chapter] = {"joy": 0, "sadness": 0, "anger": 0, "neutral": 0, "surprise": 0, "fear": 0}

    file_content[chapter][label] += 1

# print(file_content)

file_content = dict(sorted(file_content.items()))


final = []
for chapter in file_content:
    final.append({
        "chapter": chapter,
        "emotions": file_content[chapter]
    })

with open(os.path.join(__location__, "output.json"), 'w') as fo:
    json.dump(final, fo)