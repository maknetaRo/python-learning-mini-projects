import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
characters = "!#$%&*?"
numbers = "1234567890"
words = ["fizz", "buzz", "jazz", "quiz", "razz", "jeez", "jump", "java", "puja"]

print("This is a password generator.")
print("What kind of password do you want to create?")
choice = int(input("To create strong password enter 1. \
\nTo create weak, but easy to remember password enter 2."))
my_password = " "
if choice == 2:
    print("Your password is: ", random.choice(words) + random.choice(words))
elif choice == 1:
    for i in range(6):
        part = random.randrange(len(letters))
        my_password = my_password + letters[part]
        password = my_password + random.choice(characters) + random.choice(words) + random.choice(numbers)
    print("Your password is: ", password)
else:
    print("Upssss, something went wrong.")