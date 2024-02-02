import csv
import os

root_game = "FE12"

games = ["BookOne", "BookTwo"]

game_path_base = os.path.join(os.getcwd(), "data", root_game)

file_content = {
}

genders = {
    "M": "male",
    "F": "female",
    "N": "neutral",
    "A": "avatar",
    "-": "-"
}

for title in games:
    game_path = os.path.join(game_path_base, title)

    print("Running combine on " + title)

    # print(game_path)

    with open(os.path.join(game_path, "transitions.csv"), 'r') as f:
        spamreader = csv.reader(f, delimiter=',')

        next(spamreader)

        for row in spamreader:
            # print(row)
            # row[0] is tag
            if row[0] not in file_content:
                file_content[row[0]] = 0

            file_content[row[0]] += int(row[3])

# print(file_content)
            
# for tag in file_content:
#     print(tag)
#     print(file_content[tag])
            
with open(os.path.join(game_path_base, "transitions.csv"), 'w+') as output_file:

    writer = csv.writer(output_file, quoting=csv.QUOTE_NONE, delimiter=',', quotechar='', escapechar='\\')

    field = ["pairing", "from", "to", "frequency"]
    writer.writerow(field)

    for tag in file_content:
        writer.writerow([tag, genders[tag[0]], genders[tag[1]], file_content[tag]])