import subprocess
import os
import sys

# games = ["FE1", "FE2", "FE3/BookOne", "FE3/BookTwo","FE4", "FE5", "FE6", "FE7"]

# games = ["FE16/AzureMoon", "FE16/CrimsonFlower", "FE16/SilverSnow", "FE16/VerdantWind", "FE16/WhiteClouds"]

games = ["FE9", "FE10"]

# games = ["FE3/BookOne", "FE3/BookTwo", "FE12/BookTwo"]

# games = ["FE1", "FE2", "FE3/BookOne", "FE3/BookTwo", "FE11", "FE12/BookTwo", "FE15"]

# ----------------------------------
# DIALOGUE PARSER
# ----------------------------------

dialogue_parser = os.path.join(os.getcwd(), "scripts", "dialogue_parser", "dialogue_parser_json.py")

for game in games:
    command = dialogue_parser + " " + game
    subprocess.call([sys.executable, dialogue_parser, game])

# ----------------------------------
# TEXT DATA
# ----------------------------------

text_data = os.path.join(os.getcwd(), "scripts", "dialogue_parser", "text_data.py")
subprocess.call([sys.executable, text_data])

# ----------------------------------
# CHARACTER LIST
# ----------------------------------

character_list = os.path.join(os.getcwd(), "scripts", "characters_list.py")

for game in games:
    command = character_list + " " + game
    subprocess.call([sys.executable, character_list, game])

# ----------------------------------
# TRANSITIONS
# ----------------------------------

transitions = os.path.join(os.getcwd(), "scripts", "transitions.py")

for game in games:
    command = transitions + " " + game
    subprocess.call([sys.executable, transitions, game])