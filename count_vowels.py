
# Count vowels in a string

sentence = input("Enter a sentence: ")
sentence = sentence.lower()

vowel_a = int(sentence.count("a"))
vowel_e = int(sentence.count("e"))
vowel_i = int(sentence.count("i"))
vowel_o = int(sentence.count("o"))
vowel_u = int(sentence.count("u"))
vowel_y = int(sentence.count("y"))
vowels = vowel_a + vowel_e + vowel_i + vowel_o + vowel_u + vowel_y

def count_vowels(sentence):
	"""
	Returns the number of vowels  in a sentence.
	"""
	
	print("There are {} vowel(s) 'a', {} vowel(s) 'e', {} vowel(s) 'i', {} vowel(s) 'o', {} vowel(s) 'u' and {} vowel(s) 'y'.".format(vowel_a, \
		vowel_e, vowel_i, vowel_o, vowel_u, vowel_y))
	print("There are {} vowels in general.".format(vowels))

count_vowels(sentence)

# Count vowels from a web 

import requests, nltk
from bs4 import BeautifulSoup

r = requests.get("https://www.gutenberg.org/files/2701/2701-h/2701-h.htm")
r.encoding = "utf-8"

html = r.text

soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()
text = text[32000:34000]
print(text)


vowel_a = int(text.count("a"))
vowel_e = int(text.count("e"))
vowel_i = int(text.count("i"))
vowel_o = int(text.count("o"))
vowel_u = int(text.count("u"))
vowel_y = int(text.count("y"))
vowels = vowel_a + vowel_e + vowel_i + vowel_o + vowel_u + vowel_y

def count_vowels(text):
	"""
	Returns the number of vowels  in a sentence.
	"""
	
	print("There are {} vowels 'a', {} vowels 'e', {} vowels 'i', {} vowels 'o', {} vowels 'u' and {} vowels 'y'.".format(vowel_a, \
		vowel_e, vowel_i, vowel_o, vowel_u, vowel_y))
	print("There are {} vowels in general.".format(vowels))

count_vowels(text)


# Count vowels in a file
file_name = "play_play.txt"

with open(file_name) as file_object:
	contents = file_object.read()
	print(contents)
	vowel_a = int(contents.count("a"))
	vowel_e = int(contents.count("e"))
	vowel_i = int(contents.count("i"))
	vowel_o = int(contents.count("o"))
	vowel_u = int(contents.count("u"))
	vowel_y = int(contents.count("y"))
	vowels = vowel_a + vowel_e + vowel_i + vowel_o + vowel_u + vowel_y
	print("There are {} vowels 'a', {} vowels 'e', {} vowels 'i', {} vowels 'o', {} vowels 'u' and {} vowels 'y'.".format(vowel_a, \
		vowel_e, vowel_i, vowel_o, vowel_u, vowel_y))
	print("There are {} vowels in general.".format(vowels))
