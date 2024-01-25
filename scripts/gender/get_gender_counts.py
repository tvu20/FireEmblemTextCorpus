# this file generates a list of counts for each gender speaking per game

import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file_content = {}

with open(os.path.join(__location__, "speakers.json"), 'r') as f, open(os.path.join(__location__, "gender_counts.json"), 'w') as fo:
    speakers = json.load(f)
    
    for item in speakers["descriptions"]:
        # initialize gender
        gender = item["gender"]
        name = item["name"]
        if gender not in file_content:
            file_content[gender] = 0

        file_content[gender] += speakers["counts"][name]
    speakers["genderCounts"] = file_content

    json.dump(speakers, fo)