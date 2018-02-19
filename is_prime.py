def is_prime_number(num):
    """
    Check whether the given number is a prime number
    """
    if num < 2:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    else:
        return True


num = int(input("Enter a number: "))
print(is_prime_number(num))
num = int(input("Enter a number: "))
print(is_prime_number(num))
