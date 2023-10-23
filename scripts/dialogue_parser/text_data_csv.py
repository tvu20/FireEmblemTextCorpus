import csv
import sys
import os
import glob

game_path = os.path.join(os.getcwd(), "input", sys.argv[1])

output_path = os.path.join(os.getcwd(), "data", sys.argv[1])

dialogue_tags = ["intro", "battle", "end", "visit", "flashback", "recruit-visit", "recruit-battle", "recruit-conversation", "character-falls", "dialogue", "conversation", "cutscene", "boss", "recruit-talk", "battle-talk", "boss-talk"]

print("Running text data on " + sys.argv[1])

title = sys.argv[1]
title_split = title.split('/')
if len(title.split('/')) > 1:
    title = ''.join(title_split)
    print(title)

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