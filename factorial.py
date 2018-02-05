# factorial - the 28th out of 100

n = int(input("Enter a number: "))

silnia = 1
for i in range(1, n + 1):
    silnia *= i
    print("{:0}! = {:1}".format(n, silnia))


# one more

silnia = 1
for i in range(1, 101):
    silnia *= i
    print(silnia)
