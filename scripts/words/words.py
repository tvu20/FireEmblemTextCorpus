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

import os
import string
import json
from collections import Counter

game = "FE9"

transcript_path = os.path.join(os.getcwd(), "data", game, "full_transcript_cleaned.txt")

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

number_of_chapters = len(words_per_chapter)

print("Game: " + game)

print(f"Number of chapters: {number_of_chapters}")
print("Words per chapter:", words_per_chapter)
print(f"Average number of words per chapter: {sum(words_per_chapter) / number_of_chapters}")

print(f"Number of words: {len(words)}")

words_set = Counter(words)

print(f"Number of unique words: {len(words_set)}")

words_only_appearing_once = [item for item in words_set.keys() if words_set[item] == 1]

print(f"Number of words that only appear once: {len(words_only_appearing_once)}")

words_least_common = words_set.most_common()[-50:]

print("Sample of words used only once:", [x[0] for x in words_least_common])



sortedwords = sorted(words, key=len)
print("Longest word: %s" % (sortedwords[-5:],))
print("Longest word length: %d" % (len(sortedwords[-1])))

avg_word_length = sum(map(len, words))/len(words)
print("Average word length: " + str(avg_word_length))


transcript_path = os.path.join(os.getcwd(), "data", game, "full_transcript.txt")

with open(os.path.join(os.getcwd(), "data", game, "words.txt"),'w+') as fo:
    json.dump(words, fo)