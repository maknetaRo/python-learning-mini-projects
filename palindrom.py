# The 15 out of 100 mini projects
# Reverse a string and check if an input is a palindrome.
# first version
word = input("Enter a word: ")
word = word.lower()

def isPalindrome(word):
    if word == word[: : -1]:
        return "It's a palindrome."
    else:
        return "It's not a palindrome."
print(isPalindrome(word))

# second version
something = input("Enter something: ")
something = something.lower()
something = something.replace(" ", "")
something = something.replace(".", "")
def isPalindrome(something):
    reversed_str = ""
    for char in something[: : -1]:
        reversed_str = reversed_str + char
    if something == reversed_str:
        return "It's a palindrome."
    else:
        return "It's not a palindrome."

print(isPalindrome(something))

