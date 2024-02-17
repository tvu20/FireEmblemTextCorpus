import os
import glob
import sys
import string

game_path = os.path.join(os.getcwd(), "data", "other")

output_path = os.path.join(os.getcwd(), "data", "other", "textfiles")

# print("Running collect chapters on " + sys.argv[1])

with open(os.path.join(output_path, "SuperMarioBros.txt"), 'r') as file, open(os.path.join(output_path, "1.txt"), 'w+') as fo:
    for line in file:
        text = line.strip()
        
        # invalid lines
        if len(text) == 0 or line[0] == '@' or line[0] == '%' or line[0] == '#' or line[0] == '^':
            continue

        if text == "/***EOF***/":
            fo.write(line)
            continue

        removed_punctuation = text.replace("...", " ").replace("-", " ").replace("—", " ").replace("–", " ").replace("’", "").translate(str.maketrans('', '',string.punctuation)).lower().replace("…", "")
        fo.write(removed_punctuation)
        fo.write("\n")