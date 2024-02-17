
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

with open(os.path.join(__location__, "sentiments.json"), 'r') as file:

    content = json.load(file)
    main = content["Main"]

    for item in main:
        max_value = max(max_value, abs(item["sentiment"]))

    old_min = 1 
    old_max = len(main)

    for old_value in range(1, old_max + 1):
        new_value = ( (old_value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min

        file_content.append({"x": new_value, "y": main[old_value - 1]["sentiment"]})

        # print(str(new_value) + "\t" + str(main[old_value - 1]["sentiment"]))

        # print(main[old_value - 1]["sentiment"])
        # print(old_value, new_value)

    # for item in main:
    #     print(item["sentiment"])

    # print(old_max)

print(max_value)

min_value = -1 * max_value

for item in file_content:
    print(item["x"])

for item in file_content:
    old_min = -1 * max_value
    old_max = max_value
    new_min = -100 
    new_max = 100 

    new_value = ( (item["y"] - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min


    # new_value = ( (item["y"] - min_value) / (max_value - min_value) ) * (100 - (-100)) + 100
    print(new_value)
    item["y"] = new_value

print(file_content)

# old_min = 1 

# old_max = 25 

# new_min = 1 

# new_max = 100 

# for old_value in range(1, 26):

#     new_value = ( (old_value - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min

#     print(old_value, new_value)