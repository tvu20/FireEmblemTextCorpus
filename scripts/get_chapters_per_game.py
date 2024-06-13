import json
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file_content = {}

with open(os.path.join(__location__, "emotions.json"), 'r') as file:
    ans = json.load(file)

    for route in ans:
        file_content[route] = []
        for chap in ans[route]:
            file_content[route].append(chap["chapter"])

print(file_content)
