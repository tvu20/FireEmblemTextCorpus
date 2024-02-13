# IN THIS FILE:
# count number of words in a file
# count number of unique words in a file
# count words per chapter of a game
# average word length
# longest word
# number of words only used once


# in Google Colab Notebook
# https://colab.research.google.com/drive/1hiv4QeqS6U7t9cye2jwDMuXvi7f3cDVv?usp=sharing
# most common words (without stopwords)
# most common phrases (3-6 grams)
# average sentence length
# longest sentence by number of words
# number of words/unique words based on word length

import os
import string
import json
import sys
from collections import Counter

# game = sys.argv[1]
# game = "FE2"

transcript_path = os.path.join(os.getcwd(), "data", "other", "1.txt")

words = []

words_per_chapter = []
current_chapter = 0

with open(transcript_path,'r') as f:

    for line in f:
        text = line.strip()
        
        # invalid lines
        if len(text) == 0 or line[0] == '@' or line[0] == '%' or line[0] == '#' or line[0] == '^':
            continue

        # take care of end of chapter
        if text == "/***EOF***/":
            words_per_chapter.append(current_chapter)
            current_chapter = 0
            continue

        for w in text.split():
            words.append(w)
            current_chapter += 1

        # stripped = text.translate(str.maketrans('', '',string.punctuation)).lower().replace("…", "")

        # for w in stripped.split():
        #     words.append(w)
        #     current_chapter += 1

with open(os.path.join(os.getcwd(), "data", "other", "2.txt"),'w+') as fo:
    json.dump(words, fo)