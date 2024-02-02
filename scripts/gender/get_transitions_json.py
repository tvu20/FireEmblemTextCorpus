import csv
import os 
import json

games = ["FE1", "FE2", "FE3", "FE4", "FE5", "FE6", "FE7", "FE9", "FE10", "FE11", "FE12", "FE13", "FE14", "FE15", "FE16"]

game_path_base = os.path.join(os.getcwd(), "data")

file_content = {}

for title in games:
    game_path = os.path.join(game_path_base, title)

    print("Running on " + title)

    with open(os.path.join(game_path, "transitions.csv"), 'r') as f:
        spamreader = csv.reader(f, delimiter=',')

        next(spamreader)

        for row in spamreader:
            file_content[row[0]] = int(row[3])

    # print(file_content)
    with open(os.path.join(game_path, "transitions.json"), 'w+') as output_file:
        json.dump(file_content, output_file)

    file_content = {}
