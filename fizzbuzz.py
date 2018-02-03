# the fifth out of hundred pro/g/ramming challenge
# Fizz Buzz is a game for  children to teach them division. Players replace any number divisible by three with the word\
#  "fizz" and by five with the word "buzz".

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3:
        print("Fizz)
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

