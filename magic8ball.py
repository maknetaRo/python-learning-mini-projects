# Magic 8 Ball

import random

magic = [" It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it",
         "As I see it, yes", "Most likely", "Outlook good", "Yes", "signs point to yes", "Reply hazy try again",
         "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
         "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

print("Welcome to Magic 8 Ball. I'm a fortuneteller. If you don't know what to do, ask yes or no question. ")
choice = input("Do you want to play? y / n")

if choice == "n":
    print("Sorry, you are leaving.")

leave = False
while choice == "y":
    your_question = input("Enter your question: ")
    answer = random.choice(magic)
    print(answer)
    next_question = input("Do you want to play again? y / n")
    if next_question == "n":
        leave = True
        print("Bye bye")
        exit()

