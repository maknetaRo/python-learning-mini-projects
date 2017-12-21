# 3 out of 100 Pro/g/ramming Challenge
# Temperature converter

temperature = int(input("Fahrenheit degrees: "))
celsius_degrees = (temperature - 32) * 5 / 9
print("{} Fahrenheit degrees is equal to {} Celsius degrees.".format(temperature, celsius_degrees))

temperatur_cel = int(input("Celsius degrees: "))
fahrenheit_degrees = temperatur_cel * 9 / 5 + 32
print("{} Celsius degrees is equal to {} Fahrenheit degrees.".format(temperatur_cel, fahrenheit_degrees))
