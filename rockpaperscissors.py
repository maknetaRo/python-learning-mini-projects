from random import randint

print("This is Rock-Paper-Scissors game against the computer.")
print("The Rock beats the Scissors.")
print("The Paper beats the rock.")
print("The Scissors beats the paper.")

def rock_scissors_paper():
    tie = 0
    win = 0
    lose = 0
    rounds = int(input("How many rounds do you want to play? "))
    for i in range(rounds):
        random_index = randint(1, 3)
        your_choice = int(input("What do you choose: rock (1), paper (2), scissors (3)?"))
        if your_choice == 1 and random_index == 1:
            tie +=1
            print("A tie")
        elif your_choice == 1 and random_index == 2:
            lose += 1
            print("You lost. The paper beats the rock.")
        elif your_choice == 1 and random_index == 3:
            win += 1
            print("You won. The rock beats the scissors.")
        elif your_choice == 2 and random_index == 2:
            tie += 1
            print("A tie.")
        elif your_choice == 2 and random_index == 1:
            win +=1
            print("You won. The paper beats the rock.")
        elif your_choice == 2 and random_index ==3:
            lose += 1
            print("You lost. The scissors beats the paper.")
        elif your_choice == 3 and random_index == 3:
            tie += 1
            print("A tie.")
        elif your_choice == 3 and random_index == 1:
            lose += 1
            print("You lost. The rock beats the scissors.")
        elif your_choice == 3 and random_index == 2:
            win += 1
            print("You won. The scissors beats the rock.")
        else:
            print("You should enter: 1, 2 or 3.")
    print()
    if win > lose:
        print("You won. You've got {} win(s),  {} lose(s) and {} tie(s).".format(win, lose, tie))
    elif win < lose:
        print("You lost. You've got {} win(s),  {} lose(s) and {} tie(s).".format(win, lose, tie))
    elif win == lose:
        print("There is a tie. You've got {} win(s), {} lose(s) and {} tie(s).".format(win, lose, tie))
rock_scissors_paper()

once_again = "y"
while once_again == "y":
    print("\nDo you want to play one more time? ")
    once_again = input("Enter  'y' if you want to play otherwise enter  'n' ")
    once_again = once_again.lower()
    if once_again == "y":
        rock_scissors_paper()
    else:
        print("Sorry you are leaving.")




