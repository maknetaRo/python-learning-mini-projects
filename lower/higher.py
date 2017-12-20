import random

guess_taken = 0
number = random.randint(1, 51)
print("I'm thinking of a number between 1 and 50")


while guess_taken < 7:

    your_number = int(input("Can you guess?"))
    guess_taken += 1
    if your_number > 50:
        print("Your number should be between 1 and 50.")
    elif your_number > number:
        print("Your number is too high!")
        print("Try once again!")
    elif your_number < number:
        print("Your number is too low!")
        print("Try again!")
    else:
        print("You're right.")
        print("Congrats.")
        quit()

print("The number to guess was", str(number))
print("You lost!\n")


