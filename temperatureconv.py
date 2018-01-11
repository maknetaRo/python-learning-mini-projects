# 4 out of 100 Pro/g/ramming Challenge
# Temperature converter
print("What's the weater like today in the USA? ")
print("Let's conver temperature in Fahrenheit degrees into Celsius degrees.")
temperature = int(input("Fahrenheit degrees: "))
celsius_degrees = (temperature - 32) * 5 / 9
print("{} Fahrenheit degrees is equal to {} Celsius degrees.".format(temperature, celsius_degrees))
def temp_converter(celsius_degrees):
    if celsius_degrees <= -20:
        print("It's really damn cold.")
    elif -20< celsius_degrees >= -15:
        print("It's damn cold.")
    elif -15< celsius_degrees >= -10:
        print("It's really cold.")
    elif -10 < celsius_degrees >= -5:
        print("It's quite cold.")
    elif celsius_degrees == 0:
        print("It's freezing outside.")
    elif 0 < celsius_degrees >= 5:
        print("It's cold outsied.")
    elif 5 < celsius_degrees > 10:
        print("It's chilly outside.")
    elif 10 <= celsius_degrees > 15:
        print("It's cool today.")
    elif 15 <= celsius_degrees > 20:
     print("It's nice today.")
    elif 20 <= celsius_degrees > 25:
        print("It's warm.")
    elif 25 <= celsius_degrees >= 30:
        print("It's  hot today.")
    elif 30 < celsius_degrees > 35:
        print("It's quite hot.")
    elif 35 <= celsius_degrees > 40:
        print("It's damn hot.")
    elif celsius_degrees >= 40:
        print("Clothing catches fire. ")

temp_converter(celsius_degrees)


celsius_degrees = int(input("Celsius degrees: "))
fahrenheit_degrees = celsius_degrees * 9 / 5 + 32
print("{} Celsius degrees is equal to {} Fahrenheit degrees.".format(celsius_degrees, fahrenheit_degrees))

temp_converter(celsius_degrees)
