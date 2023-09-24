import os
import re
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

old_file_path = os.path.join(__location__, '01-MarthEmbarks.txt')

new_file_path = os.path.join(__location__, 'mynewfile.json')

file_content = {}

normal_tags = ["intro", "battle", "end", "visit", "flashback", "recruit-visit", "recruit-battle", "character-falls", "dialogue"]
narration_tags = ["opening", "narration"]
people_tags = ["boss", "recruit-talk", "battle-talk"]


# handles narration text - no speaker information
def narration_tag(text, tag):
    file_content[tag].append(text)

# handles normal conversations - speaker and dialogue
def normal_tag(text, tag):
    speaker = ''
    line = ''
    colon_split = text.split(": ")

    if len(colon_split) > 1:
        speaker = colon_split.pop(0).title()
        line = ": ".join(colon_split)

    if speaker not in file_content["speakers"]:
        file_content["speakers"].append(speaker)

    file_content[tag].append({
        "speaker": speaker,
        "line": line
    })

# handles recruit conversations - info on recruiter/recruitee
def recruit_talk(text, recruiter, recruit):
    speaker = ''
    line = ''
    colon_split = text.split(": ")

    if len(colon_split) > 1:
        speaker = colon_split.pop(0).title()
        line = ": ".join(colon_split)
    
    if speaker not in file_content["speakers"]:
        file_content["speakers"].append(speaker)

    file_content[tag].append({
        "speaker": speaker,
        "line": line,
        "recruiter": recruiter,
        "recruit": recruit
    })

# handles battle conversations - info on who is speaking
def battle_talk(text, person_1, person_2):
    speaker = ''
    line = ''
    colon_split = text.split(": ")

    if len(colon_split) > 1:
        speaker = colon_split.pop(0).title()
        line = ": ".join(colon_split)

    if speaker not in file_content["speakers"]:
        file_content["speakers"].append(speaker)

    file_content[tag].append({
        "speaker": speaker,
        "line": line,
        "person_1": person_1,
        "person_2": person_2
    })

# handles boss conversations - special cases
def boss(text, unit, boss):
    speaker = ''
    line = ''
    colon_split = text.split(": ")

    if len(colon_split) > 1:
        speaker = colon_split.pop(0).title()
        line = ": ".join(colon_split)
    
    if speaker not in file_content["speakers"]:
        file_content["speakers"].append(speaker)

    if len(unit) == 0:
        file_content[tag].append({
            "speaker": speaker,
            "line": line,
        })
    else: 
        file_content[tag].append({
            "speaker": speaker,
            "line": line,
            "unit": unit,
            "boss": boss
        })


# reading and writing to JSON file
with open(old_file_path, 'r') as f, open(new_file_path, 'w') as file:
    filename = old_file_path.split('/')[-1].split(".")[0]
    file_info = filename.split("-")

    file_content["chapter"] = int(file_info[0])
    file_content["title"] = " ".join(re.split('(?<=.)(?=[A-Z])', file_info[1]))

    file_content["speakers"] = []
    # file_content["transitions"] = ""

    tag = ''
    subtag = False
    person_1 = ''
    person_2 = ''

    for line in f:
        text = line.strip()
        if len(text) == 0:
            if tag in people_tags:
                person_1 = ''
                person_2 = ''

            # file_content["transitions"] += "-"
            continue

        # NEW TAG
        if line[0] == '@':
            tag = line.split('@')[1].strip().lower()
            file_content[tag] = []
            # print(tag)
            continue

        # NEW SUBTAB
        if line[0] == '%':
            persons = text[1:].split(",")
            person_1 = persons[0]
            person_2 = persons[1]
            continue

        if tag in narration_tags:
            narration_tag(text, tag)
        elif tag in normal_tags:
            normal_tag(text, tag)
        elif tag == "recruit-talk":
            recruit_talk(text, person_1, person_2)
        elif tag == "battle-talk":
            battle_talk(text, person_1, person_2)
        elif tag == "boss":
            boss(text, person_1, person_2)
        else:
            continue

    json.dump(file_content, file)

