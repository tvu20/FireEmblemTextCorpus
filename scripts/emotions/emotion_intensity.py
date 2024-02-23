
# if I have 25 data points
# and I want to convert to a graph with 100 range on x axis

# point 1 -> x = 0
# point 2 -> x = 4
# ...

# point 24 -> 92
# point 25 -> 96

# old_value = 25

import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

data = []

old_max = 25 
new_min = 1 
new_max = 100 

file_content = []

max_value = 0

with open(os.path.join(__location__, "input.json"), 'r') as file:

    content = json.load(file)

    old_min = 1 
    old_max = len(content)

    for old_value in range(1, old_max + 1):

        item = content[old_value - 1]

        total = item["emotions"]["joy"] + item["emotions"]["sadness"] + item["emotions"]["anger"] + item["emotions"]["surprise"] + item["emotions"]["fear"]

        new_value = ( (old_value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min

        file_content.append({"x": new_value, "y": total / (total + item["emotions"]["neutral"])})

# print(file_content)

# old_min = 1 

# old_max = 25 

# new_min = 1 

# new_max = 100 

# for old_value in range(1, 26):

#     new_value = ( (old_value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min

#     print(old_value, new_value)

# import json
# import os

# __location__ = os.path.realpath(
#     os.path.join(os.getcwd(), os.path.dirname(__file__)))

# file_content = []

# new_min = 1 
# new_max = 100 

# with open(os.path.join(__location__, "input.json"), 'r') as f:
#     arr = json.load(f)

#     for i, item in enumerate(arr):
#         total = item["emotions"]["joy"] + item["emotions"]["sadness"] + item["emotions"]["anger"] + item["emotions"]["surprise"] + item["emotions"]["fear"]

#         file_content.append({"x": i, "y": total / (total + item["emotions"]["neutral"])})

with open(os.path.join(__location__, "intensity.json"), 'w') as fo:
    json.dump(file_content, fo)