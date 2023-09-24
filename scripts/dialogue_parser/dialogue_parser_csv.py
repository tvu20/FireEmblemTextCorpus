import csv
import re
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

old_file_path = os.path.join(__location__, '01-MarthEmbarks.txt')

new_file_path = os.path.join(__location__, 'mynewfile.txt')

with open(old_file_path, 'r') as f, open(new_file_path, 'w') as file:
    filename = old_file_path.split('/')[-1].split(".")[0]
    file_info = filename.split("-")

    chapter_number = int(file_info[0])
    chapter_title = " ".join(re.split('(?<=.)(?=[A-Z])', file_info[1]))

    writer = csv.writer(file, quoting=csv.QUOTE_NONE, delimiter='|', quotechar='')
    field = ["tag", "speaker", "line", "person_1", "person_2"]
    writer.writerow(field)

    tag = ''
    subtag = False
    person_1 = ''
    person_2 = ''

    for line in f:
        text = line.strip()
        if len(text) == 0:
            continue

        # NEW TAG
        if line[0] == '@':
            tag = line.split('@')[1].strip()
            print(tag)
            continue

        # NEW SUBTAB
        if line[0] == '%':
            persons = text[1:].split(",")
            person_1 = persons[0]
            person_2 = persons[1]
            continue

        colon_split = text.split(": ")

        if len(colon_split) > 1:
            speaker = colon_split.pop(0)
            text = ": ".join(colon_split)
        else:
            speaker = "Narrator"


        writer.writerow([tag, speaker, text, person_1, person_2])