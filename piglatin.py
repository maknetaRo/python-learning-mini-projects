
vowels = "aeiouy"
print("Let's translate some words together.")
word = input("Enter a word: ")
word = word.lower()

pig = "ay"

if  len(word) > 0 and word.isalpha():
    word.lower()
    first = word[0]
    if first in vowels:
        new_word = word + pig
        print(new_word)
    else:
        for letter in word:
            if letter in vowels:
                slash = word.index(letter)
                break
        beginning = word[:slash]
        new_word = word[slash:] + beginning + pig
        print(new_word)


