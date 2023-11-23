import os
import glob
import sys
import string

game_path = os.path.join(os.getcwd(), "input", sys.argv[1])

output_path = os.path.join(os.getcwd(), "data", sys.argv[1])

print("Running collect chapters on " + sys.argv[1])

with open(os.path.join(output_path, "full_transcript.txt"), 'w+') as file:
    for filename in glob.glob(os.path.join(game_path, "transcripts", "*.txt")):

        with open(filename, 'r') as f:
            for line in f:
                line = line.replace("…", "...")
                file.write(line)

        file.write("\n")
        file.write("/***EOF***/\n")

# get cleaned transcript

with open(os.path.join(output_path, "full_transcript.txt"), 'r') as file, open(os.path.join(output_path, "full_transcript_cleaned.txt"), 'w+') as fo:
    for line in file:
        text = line.strip()
        
        # invalid lines
        if len(text) == 0 or line[0] == '@' or line[0] == '%' or line[0] == '#' or line[0] == '^':
            continue

        if text == "/***EOF***/":
            fo.write(line)
            continue

        split_speaker = text.split(": ")
        if len(split_speaker) < 2:
            removed_punctuation = text.replace("...", " ").replace("-", " ").replace("’", "").translate(str.maketrans('', '',string.punctuation)).lower()
            fo.write(removed_punctuation)
            fo.write("\n")
            continue

        new_line = split_speaker[1:]
        new_line = ' '.join(new_line)
        removed_punctuation = new_line.replace("...", " ").replace("-", " ").replace("’", "").translate(str.maketrans('', '',string.punctuation)).lower().replace("…", "")
        fo.write(removed_punctuation)
        fo.write("\n")