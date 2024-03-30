import nltk
import itertools
from nltk.corpus import words
import json

word_list = set(words.words())  # Using a set for unique words

# Create a dictionary where each word is a key with True as its value
word_dict = {word: True for word in word_list}

# Save the dictionary as JSON
with open('word_dict.json', 'w') as json_file:
    json.dump(word_dict, json_file)