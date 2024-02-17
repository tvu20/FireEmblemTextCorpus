import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file_content = []

with open(os.path.join(__location__, "sentiment.txt"), 'r') as file:
    for line in file:
        spl = line.strip().split("	")

        # print(spl)
        file_content.append({"x": spl[0], "y": spl[1]})

print(file_content)