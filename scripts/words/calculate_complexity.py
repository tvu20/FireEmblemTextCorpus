import os
import glob
import sys
import string
import re

# string_test = "Oh. Master Wendell. Yes, it's you."

# string_test = string_test.replace("!", ".").replace("?", ".").replace("...", ".")

# print(string_test)

# sentences = string_test.split(".")

# print(sentences)

# print(len(sentences) - 1)

# words = string_test.split(" ")
# print(words)
# print(len(words))

# print(len(re.findall('[a-zA-Z]', string_test)))

# print("Running collect chapters on " + sys.argv[1])

current_sentences = 0
current_words = 0
current_characters = 0

total_sentences = 0
total_words = 0
total_characters = 0

print("TEXT COMPLEXITY")
print("Sentences, words per sentence, characters per word, words, characters")


# print(os.path.join(os.getcwd(), "data", sys.argv[1], "full_transcript.txt"))
# with open(os.path.join(os.getcwd(), "data", sys.argv[1], "full_transcript.txt"), 'r') as file:

with open(os.path.join(os.getcwd(), "data", "other", "textfiles", "SuperMarioBros.txt"), 'r') as file:
    for line in file:
        text = line.strip()
        
        # invalid lines
        if len(text) == 0 or line[0] == '@' or line[0] == '%' or line[0] == '#' or line[0] == '^':
            continue

        if text == "/***EOF***/":
            words_per_sentence = str(round(current_words / current_sentences, 2))
            chars_per_word = str(round(current_characters / current_words, 2))
            print(current_sentences, words_per_sentence, chars_per_word, current_words, current_characters)
            # fo.write(line)

            current_sentences = 0
            current_words = 0
            current_characters = 0
            continue

        string_test = text.replace("!", ".").replace("?", ".").replace("...", ".")

        if "." in string_test:
            sentences = string_test.split(".")
            current_sentences += len(sentences) - 1
            total_sentences += len(sentences) - 1

        words = string_test.split(" ")
        current_words += len(words)
        total_words += len(words)

        current_characters += len(re.findall('[a-zA-Z]', string_test))
        total_characters += len(re.findall('[a-zA-Z]', string_test))

print("Final results")
print(total_sentences, str(round(total_words / total_sentences, 2)), str(round(total_characters / total_words, 2)), total_words, total_characters)