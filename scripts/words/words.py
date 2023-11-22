# count number of words in a file
# count number of unique words in a file
# count most common words in a file
# count words per chapter of a game
# most common phrases
# speaker counts
# average sentence length
# average word length
# longest word
# longest sentence by number of words
# number of words only used once

import os
import string
from collections import Counter

game = "FE1"

transcript_path = os.path.join(os.getcwd(), "data", game, "full_transcript.txt")

# delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum())

# print(delchars)

# words = ["ldkjflkdjfs"]

# mystring = "Morzas: Basilisk! I call upon your power! Burn these arrogant humans to ash! i to you"

# newstr = mystring.translate(str.maketrans('', '',string.punctuation)).lower()

# for w in newstr.split():
#     words.append(w)

# print(words)

# print(Counter(words))

# print(mystring)

# print(scrunched)

words = []

with open(transcript_path,'r') as f:

    for line in f:
        text = line.strip()
        
        # invalid lines
        if len(text) == 0 or line[0] == '@' or line[0] == '%' or line[0] == '#' or line[0] == '^':
            continue

        stripped = text.translate(str.maketrans('', '',string.punctuation)).lower()

        for w in stripped.split():
            words.append(w)



    # words = [word for line in f
    #          for word in line.strip().split()]
print(f"Number of words: {len(words)}")

words_set = Counter(words)

print(f"Number of unique words: {len(words_set)}")

print(words_set.most_common(20))