sentence = input("Please enter a sentence: ")
space_count = 0
for character in sentence:
	if character == " ":
		space_count = space_count + 1
number_of_words = space_count + 1
print("The user entered: ", sentence, sep =" ")
print("The number of words in the sentence is", number_of_words, sep = " ")


sentence = input("Enter a sentence: ")
print(sentence)
words = sentence.split()
print(words)
number_of_words = len(words)
print(number_of_words)