import subprocess
import os
import sys

games = ["FE1", "FE2", "FE3/BookOne", "FE3/BookTwo", "FE11", "FE12/BookTwo", "FE15"]

dialogue_parser = os.path.join(os.getcwd(), "scripts", "dialogue_parser", "dialogue_parser_json.py")

for game in games:
    command = dialogue_parser + " " + game
    subprocess.call([sys.executable, dialogue_parser, game])

character_list = os.path.join(os.getcwd(), "scripts", "characters_list.py")

for game in games:
    command = character_list + " " + game
    subprocess.call([sys.executable, character_list, game])

transitions = os.path.join(os.getcwd(), "scripts", "transitions.py")

for game in games:
    command = transitions + " " + game
    subprocess.call([sys.executable, transitions, game])