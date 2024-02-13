import os
import string
import json
import sys
from collections import Counter
import operator

transcript_path = os.path.join(os.getcwd(), "scripts", "words", "phrases.txt")

phrases_obj = {}

current_game = ""

with open(transcript_path,'r') as f:

    for line in f:
        text = line.strip()
        
        # name of game
        if text[0] == "*":
            current_game = text[1:]
            continue

        splits = text.split()
        # print(splits)

        counts = int(splits[0])
        phrase = ' '.join(splits[1:])
        
        # phrase doesn't exist
        if phrase not in phrases_obj:
            phrases_obj[phrase] = {"count": 0, "games": []}
        phrases_obj[phrase]["count"] += counts
        phrases_obj[phrase]["games"].append(current_game)

file_content = []
for item in phrases_obj:
    file_content.append({"text": item, "value": phrases_obj[item]["count"], "games": phrases_obj[item]["games"]})

file_content = sorted(file_content, key=lambda k: k['value'], reverse=True)
        
# print(phrases_obj)

# number_of_chapters = len(words_per_chapter)

# print("Game: " + game)

# print(f"Number of chapters: {number_of_chapters}")
# print("Words per chapter:", words_per_chapter)
# print(f"Average number of words per chapter: {sum(words_per_chapter) / number_of_chapters}")

# print(f"Number of words: {len(words)}")

# words_set = Counter(words)

# print(f"Number of unique words: {len(words_set)}")

# words_only_appearing_once = [item for item in words_set.keys() if words_set[item] == 1]

# print(f"Number of words that only appear once: {len(words_only_appearing_once)}")

# words_least_common = words_set.most_common()[-50:]

# print("Sample of words used only once:", [x[0] for x in words_least_common])



# sortedwords = sorted(words, key=len)
# # print("Longest dictionary word: %s" % (sortedwords[-1],))
# print("Longest dictionary word: %s" % (sortedwords[-5:],))
# print("Longest dictionary word length: %d" % (len(sortedwords[-1])))

# avg_word_length = sum(map(len, words))/len(words)
# print("Average word length: " + str(avg_word_length))


# transcript_path = os.path.join(os.getcwd(), "data", game, "full_transcript.txt")

with open(os.path.join(os.getcwd(), "scripts", "words", "phrases.json"),'w+') as fo:
    json.dump(file_content, fo)