# My first project for 100 Pro/g/ramming Challenge v1.3
# 1. the program chooses names from the list created by me.

import random

f_first_names = ["Ala", "Ela", "Zosia", "Jola", "Jagoda", "Beata", "Martyna", \
"Iwona",  "Kinga", "Ania", "Marta", "Tosia", "Julia","Irmina", "Karolina", \
"Maja",  "Paulina", "Patrycja", "Sandra", "Kasia"]
f_last_names = ["Kowalska", "Turowicz", "Mickiewicz", "Macierzanka", "Martynkiewicz",  "Ewitkowicz", \
             "Krysteńko",  "Puchałowicz", "Ortegowska",  "Dziemianko",  "Gryczyńska",  "Grecka",
             "Puryńsko",  "Prawdzik", "Mika", "Milewicz", "Szymańska",  "Truskawko", "Kryk", \
             "Połajko"]

m_first_names = ["Adam", "Staszek", "Grześ", "Alan", "Gracjan", "Michał", "Damian", "Darek",\
                 "Marek", "Mateusz", "Krystian", "Dawid", "Sebastian", "Patryk", "Miłosz", \
                 "Julek", "Olaf", "Kacper", "Paweł", "Jakub"]
m_last_names = ["Kowalski", "Michnik", "Mazowiecki", "Narutowicz", "Piechociński", "Pływaczek", "Sporek", \
                "Frenczyk", "Opatek", "Plustek", "Plawik", "Geniowski", "Pawłowski", "Andruczyk", "Praczyk", \
                "Alowski", "Kruszewski", "Krawczyk", "Rusiecki", "Zrombkowski"]



# 2. This is the first version of random name generator -
print("This is a Polish names' random generator.")
# Femine name:
print("Your name is ", random.choice(f_first_names), random.choice(f_last_names) + ".")
# Masculine name:
print("Your name is", random.choice(m_first_names), random.choice(m_last_names) + ".")
print("**********************************************")
# 3. This is the second version of a name generator form list with user input
gender  = input("Man or woman? (f / m) ")

name = None
surname = None

if gender == "f" or gender == "woman":
    name = random.choice(f_first_names)
    surname = random.choice(f_last_names)
else:
    name = random.choice(m_first_names)
    surname = random.choice(m_last_names)
print("Your name is {} {}".format(name, surname) + ".")

# 4. This is a baby names generator based on string library.
import string, random

vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxz"
letters = string.ascii_lowercase
first_input = input("Give the first letter - \"v\" for a vowel, \"c\" for a consonant, \"l\" for any other letter.")
second_input = input("Give the second letter - \"v\" for a vowel, \"c\" for a consonant, \"l\" for any other letter.")
third_input = input("Give the third letter - \"v\" for a vowel, \"c\" for a consonant, \"l\" for any other letter.")
fourth_input = input("Give the fourth letter - \"v\" for a vowel, \"c\" for a consonant, \"l\" for any other letter.")
fifth_input = input("Give the fifth letter - \"v\" for a vowel, \"c\" for a consonant, \"l\" for any other letter.")
sixth_letter = random.choice(vowels)

def generator():
    if first_input == "v":
        first_letter = random.choice(vowels)
    elif first_input == "c":
        first_letter = random.choice(consonants)
    elif first_input == "l":
        first_letter = random.choice(letters)
    else:
        first_letter = first_input

    if second_input == "v":
        second_letter = random.choice(vowels)
    elif second_input == "c":
        second_letter = random.choice(consonants)
    elif second_input == "l":
        second_letter = random.choice(letters)
    else:
        second_letter = second_input

    if third_input == "v":
        third_letter = random.choice(vowels)
    elif third_input == "c":
        third_letter = random.choice(consonants)
    elif third_input == "l":
        third_letter = random.choice(letters)
    else:
        third_letter = third_input

    if fourth_input == "v":
        fourth_letter = random.choice(vowels)
    elif fourth_input == "c":
        fourth_letter = random.choice(consonants)
    elif fourth_input == "l":
        fourth_letter = random.choice(letters)
    else:
        fourth_letter = fourth_input

    if fifth_input == "v":
        fifth_letter = random.choice(vowels)
    elif fifth_input == "c":
        fifth_letter = random.choice(consonants)
    elif fifth_input == "l":
        fifth_letter = random.choice(letters)
    else:
        fifth_letter = fifth_input

    baby_name = first_letter + second_letter + third_letter + fourth_letter + fifth_letter + sixth_letter
    return(baby_name.title())

print("Your baby's name is {}".format(generator()) + ".")
