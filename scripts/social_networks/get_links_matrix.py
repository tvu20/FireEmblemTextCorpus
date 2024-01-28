# this file generates a list of links based on character pairing matrix. places output in links.json

import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

file_content = {}
pairs = []

with open(os.path.join(__location__, "nodes.json"), 'r') as f, open(os.path.join(__location__, "matrix.csv"), 'r') as fmatrix, open(os.path.join(__location__, "links.json"), 'w') as fo:

    file_content = json.load(f)
    file_content["links"] = []

    line = fmatrix.readline().strip()
    names_list = line.split(',')

    while line != "":

        row = line.split(',')
        name_1 = row[0].strip()

        for i, cell in enumerate(row):
            if cell.strip() == 'x':
                name_2 = names_list[i].strip()

                if (name_1, name_2) not in pairs and (name_2, name_1) not in pairs:
                    pairs.append((name_1, name_2))



        line = fmatrix.readline().strip()
   
    file_content["pairs"] = pairs

    for p1, p2 in pairs:
        file_content["links"].append({"source": p1, "target": p2})



    json.dump(file_content, fo)
