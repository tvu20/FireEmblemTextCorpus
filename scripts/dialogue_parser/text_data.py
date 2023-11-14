import csv
import sys
import os
import glob

# games = ["FE1", "FE2", "FE3/BookOne", "FE3/BookTwo", "FE4", "FE5", "FE6", "FE7"]

# games = ["FE16/AzureMoon", "FE16/CrimsonFlower", "FE16/SilverSnow", "FE16/VerdantWind", "FE16/WhiteClouds"]

games = ["FE5"]

# games = ["FE3/BookOne", "FE3/BookTwo", "FE12/BookTwo"]

# games = ["FE1", "FE2", "FE3/BookOne", "FE3/BookTwo", "FE11", "FE12/BookTwo", "FE15"]

game_path_base = os.path.join(os.getcwd(), "input")

output_path_base = os.path.join(os.getcwd(), "data")

dialogue_tags = ["intro", "battle", "end", "visit", "flashback", "recruit-visit", "recruit-battle", "recruit-conversation", "character-falls", "dialogue", "conversation", "cutscene", "boss", "recruit-talk", "battle-talk", "boss-talk"]

for title in games:
    game_path = os.path.join(game_path_base, title)
    output_path = os.path.join(output_path_base, title)

    print("Running text data on " + title)

    title_split = title.split('/')
    if len(title.split('/')) > 1:
        title = ''.join(title_split)

    output_file = open(os.path.join(output_path, title + ".csv"), 'w+')

    writer = csv.writer(output_file, quoting=csv.QUOTE_NONE, delimiter='|', quotechar='')

    writer.writerow(["game", "chapter", "speaker", "text", "tag"])

    for filename in glob.glob(os.path.join(game_path, "transcripts", "*.txt")):
        chapter = filename.split('/')[-1].split(".")[0]

        with open(filename, 'r') as f:
            tag = ''

            for line in f:
                text = line.strip()

                # skip everything that's not dialogue
                if len(text) == 0 or \
                    line[0] == '%' or \
                    line[0] == '#' or \
                    line[0] == '^':
                    continue

                # update tag if needed
                if line[0] == '@':
                    tag = line.split('@')[1].strip().lower()
                    continue

                # if narration tag continue
                if tag not in dialogue_tags:
                    continue 

                # now handling parsing text
                speaker = ''
                line = ''
                colon_split = text.split(": ")

                if len(colon_split) > 1:
                    speaker = colon_split.pop(0).title()
                    line = ": ".join(colon_split)

                writer.writerow([title, chapter, speaker, line, ""])


    output_file.close()