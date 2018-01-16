# Love Calculator
vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxyz"
love = "love"

print("This is a love calculator.")
name_one = input("Enter your name: ")
name_two = input("Enter your partner's name: ")
name_one = name_one.lower()
name_two = name_two.lower()

num_vowels1 = 0
num_vowels2 = 0
num_cons1 = 0
num_cons2 = 0
points = 0

love_one = 0
love_two = 0

# the same length
if len(name_one ) == len(name_two):
    points += 20


# both start from the same letter
if name_one[0] == name_two[0]:
    points += 20


# both start from the vowel
if (name_one[0] in vowels) and (name_two[0] in vowels):
    points += 10

# both start from the consonant
if (name_one[0] in consonants) and (name_two[0] in consonants):
    points += 5


# the same number of vowels or consonants
for letter in name_one:
    if letter in vowels:
        num_vowels1 += 1
    elif letter in consonants:
        num_cons1 += 1

for letter in name_two:
    if letter in vowels:
        num_vowels2 += 1
    elif letter in consonants:
        num_cons2 += 1

if num_vowels1 == num_vowels2:
    points += 12


if num_cons1 == num_cons2:
    points += 12


# letters in love
for letter in name_one:
    if letter in love:
        love_one += 1

for letter in name_two:
    if letter in love:
        love_two += 1


if love_one != 0 and  love_two != 0:
    points += 7


# score
wynik = (points / 89) * 100
wynik = round(wynik, 0)
print("Your score is", wynik)
if wynik > 85:
    print("You are an ideal couple.")
elif wynik > 60:
    print("You need to work a bit.")
elif wynik > 40:
    print("A lot of work to be together.")
elif wynik <= 40:
    print("No chance.")







