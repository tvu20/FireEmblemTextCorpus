import os
import re
import json
import glob
import sys

game_path = os.path.join(os.getcwd(), "data", sys.argv[1])

file_content = {}

normal_tags = ["intro", "battle", "end", "visit", "flashback", "recruit-visit", "recruit-battle", "character-falls", "dialogue"]
narration_tags = ["opening", "narration"]
people_tags = ["boss", "recruit-talk", "battle-talk"]


# ----------------------------------
# GETTING GENDER INFORMATION
# ----------------------------------
gender_info = {}
with open(os.path.join(game_path, "genders.json"), 'r') as f:
    gender_info = json.load(f)


# -----------------------
# HELPER FUNCTIONS
# -----------------------

# updates speaker file
def update_speaker(speaker):
    if speaker not in file_content["speakers"]:
        file_content["speakers"].append(speaker)
        file_content["dialogue_counts"][speaker] = 1
    else:
        file_content["dialogue_counts"][speaker] += 1

    update_gender(speaker)

# update information relating to gender
def update_gender(speaker):
    gender = gender_info[speaker]
    file_content["transitions"] += gender
    file_content["gender_counts"][gender] += 1


# -----------------------
# HANDLING TAGS
# -----------------------

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

    update_speaker(speaker)

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
    
    update_speaker(speaker)

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

    update_speaker(speaker)

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
    
    update_speaker(speaker)

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



# ----------------------------------
# WRITING TO CHAPTER JSON FILES
# ----------------------------------

# reading and writing to JSON file

for filename in glob.glob(os.path.join(game_path, "transcripts", "*.txt")):
    file_without_type = filename.split('/')[-1].split(".")[0]

    file_content = {}

    with open(filename, 'r') as f, open(os.path.join(game_path, "chapters", file_without_type + ".json"), 'w') as file:

        file_info = file_without_type.split("-")
        file_content["chapter"] = file_info[0]
        file_content["title"] = " ".join(re.split('(?<=.)(?=[A-Z])', file_info[1]))

        file_content["speakers"] = []
        file_content["dialogue_counts"] = {}
        file_content["gender_counts"] = {
            "M": 0,
            "F": 0,
            "N": 0
        }
        file_content["lines"] = 0
        file_content["transitions"] = ""

        tag = ''
        subtag = False
        person_1 = ''
        person_2 = ''

        for line in f:
            text = line.strip()

            # blank line
            if len(text) == 0:
                if tag in people_tags:
                    person_1 = ''
                    person_2 = ''

                file_content["transitions"] += "-"

                # file_content["transitions"] += "-"
                continue

            # NEW TAG
            if line[0] == '@':
                tag = line.split('@')[1].strip().lower()
                file_content[tag] = []
                continue

            # NEW SUBTAB
            if line[0] == '%':
                persons = text[1:].split(",")
                person_1 = persons[0]
                person_2 = persons[1]
                continue

            file_content["lines"] += 1

            # handle dialogue lines
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