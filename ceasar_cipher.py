
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(len(alphabet))
key = alphabet[3:26] + alphabet[0:3] + alphabet[29:]+ alphabet[26:29]
print(len(key))
print(key)
table = "".maketrans(alphabet, key)
message = input("Enter a message: ")

message = message.translate(table)
print("Your message:" + message)