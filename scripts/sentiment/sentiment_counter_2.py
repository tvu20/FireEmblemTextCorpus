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
        file_content[chapter] = {"positive": 0, "negative": 0, "neutral": 0}

    file_content[chapter][label] += 1

# print(file_content)

file_content = dict(sorted(file_content.items()))

final = []

for item in file_content:
    chapter_info = {}
    chapter_info["chapter"] = item
    chapter_info["positive"] = file_content[item]["positive"]
    chapter_info["negative"] = file_content[item]["negative"]
    chapter_info["neutral"] = file_content[item]["neutral"]

    chapter_info["sentiment"] = chapter_info["positive"] + (-1 * chapter_info["negative"]) 

    final.append(chapter_info)

with open(os.path.join(__location__, "output.json"), 'w') as fo:
    json.dump(final, fo)