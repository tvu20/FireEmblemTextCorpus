import random
import os

path = os.path.join(os.getcwd(), "scripts", "randomizer_input.txt")
lines = open(path).readlines()
random.shuffle(lines)
open(path, 'w').writelines(lines)