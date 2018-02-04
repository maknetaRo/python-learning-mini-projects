a = 0
b = 1
number = int(input("Enter No.of Fibonacci to be generated: "))

if number <= 0:
    print("Not possible")
elif number == 1:
    print(a)
elif number >= 2:
    print("{}, {}".format(a, b), end=", ")
    for i in range(2, number):
        c = a + b
        print("{}".format(c), end=", ")
        a = b
        b = c

