# This program finds anagrams and check which of them are real English words

import itertools
import nltk
nltk.download("words")
from nltk.corpus import words
is_anagram = input("Enter a word to create anagrams: ")
perms = set(["".join(perm) for perm in itertools.permutations(is_anagram)])
print(perms) # prints all anagrams

# Checks which of them are real English words
for element in perms:
    if element in words.words():
        print(element)

# The program checks if two words are anagrams:
str1 = input("Enter a word: ")
str2 = input("Enter another word: ")

def is_anagram(str1, str2):
    list_str1 = list(str1)
    list_str1.sort()
    list_str2 = list(str2)
    list_str2.sort()
    return (list_str1 == list_str2)

print(is_anagram(str1, str2))