# Encrypt / Decrypt Algorithm
print("First version: ")
alphabet = "aeiou"
key = "12345"
table = "".maketrans(alphabet, key)


message = input("Enter a short message: ")
message = message.lower()

message = message.translate(table)

print(message.capitalize())
table = "".maketrans(key, alphabet)
print("decrypt")
message = message.translate(table)
print(message.capitalize())


print("Second version: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = alphabet[: : -1]

message = input("Enter a short message: ")
message = message.lower()

for c in message:
    if c.isalpha():
        print(key[alphabet.index(c)], end="")
    else:
        print(c, end="")
