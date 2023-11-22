import os
import glob
import sys

game_path = os.path.join(os.getcwd(), "input", sys.argv[1])

output_path = os.path.join(os.getcwd(), "data", sys.argv[1])

with open(os.path.join(output_path, "full_transcript.txt"), 'w+') as file:
    for filename in glob.glob(os.path.join(game_path, "transcripts", "*.txt")):

        with open(filename, 'r') as f:
            for line in f:
                file.write(line)