import nltk
import itertools
from nltk.corpus import words

# Convert the word list to a set for O(1) lookup time
word_list = set(words.words())

# Example set of letters
letters = "example"

# Generate all permutations of these letters of a certain length (e.g., 5 letters long)
permutations = itertools.permutations(letters, 5)

# Convert the tuples from itertools.permutations into strings
permutations_as_strings = [''.join(permutation) for permutation in permutations]

# Filter the permutations to only include valid English words
valid_permutations = [word for word in permutations_as_strings if word in word_list]

print(valid_permutations)
