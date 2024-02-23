import json
import os
from statistics import mean 

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

temp_arr = {}

for i in range(1, 101):
    temp_arr[i] = []

# print(temp_arr)

file_content = []

with open(os.path.join(__location__, "curves.json"), 'r') as file:
    data = json.load(file)

    for game, values in data.items():
        for item in values:
            index = int(round(item["x"]))
            temp_arr[index].append(item["y"])
    # for attr, value in data.items():
    #     print(attr, value)

    print(temp_arr)

    for index, values in temp_arr.items():
        if len(values) == 0: continue
        # if len(values) == 0 or len(values) == 1: continue
        avg = mean(values) 

        file_content.append({"x": index, "y": avg})

print(file_content)