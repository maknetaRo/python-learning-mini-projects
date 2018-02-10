"""
Project number 33 - converting integers into words using lists
"""
first_numbers = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split(" ")
tens = "ten twenty thirty forty fifty sixty seventy eighty ninety".split(" ")


def number_to_word(number):
    """
    Converts number into words, when the number is one thousand or less.

    """
    if number < 20:
        number = first_numbers[number]

    elif number < 100 and number % 10 == 0:
        number = tens[int(number/10 -1)]

    elif number < 1000 and number % 10 == 0:
        number = first_numbers[int(number / 100)] + " hundred"

    elif number == 1000:
        number = "one thousand"

    elif number < 100 and number % 10 != 0:
        number = tens[int(number // 10 - 1)] + "-" + first_numbers[number % 10]

    elif number < 1000:
        if number % 100 < 20:
            number = first_numbers[int(number // 100)] + " hundred and " + first_numbers[number % 100]
        else:
            number = first_numbers[int(number // 100)] + " hundred and " + tens[int(number % 100 // 10 - 1)] + \
                 "-" + first_numbers[int(number % 10)]

    return number



def main():
    print(number_to_word(999))
    print(number_to_word(76))
    print(number_to_word(8))
    print(number_to_word(100))
    print(number_to_word(356))


if __name__ == "__main__":
    main()
