# check if word is a palindrome and  then print out all palindroms
import random

palindorms = []

question = input("Do you want to check if your word or sentence is a palindorme? y / n")
if question == "n":
    print("Sorry you are leaving. ")

leave = False
while question == "y":
    word = input("Enter a word: ")
    word = word.lower()
    word = word.replace(" ", "")
    word = word.replace(".", "")
    if word == word[: : -1]:
        print("It's a palindrome.")
        palindorms.append(word)
    else:
        print("It's not a palindrome.")
    next_question = input("Do you want to check more words: ? y / n")
    if next_question == "n":
        leave = True
        print("These words or sentences are palindromes: ", palindorms)
        break

print("It's a Random Palindrome Generator. It chooses one palindrome from a list created by you. ")
print(random.choice(palindorms))



