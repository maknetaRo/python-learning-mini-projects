# Convert Decimal to Binary

while True:
	print("Enter 'x' for exit.")
	dec = input("Enter number in Decimal Format: ")
	if dec == "x":
		break
	else:
		decimal = int(dec)
		print(decimal, "in Binary =", bin(decimal), "\n")

# another way
def dec_to_bi(x):
	return int(bin(x)[2:])

print(dec_to_bi(7))

# one more

numb = 121 
binary = ""

while(numb):
	if  (numb % 2 == 0):
		binary += "0"
	else:
		binary += "1"
	numb = numb // 2

"".join(reversed(binary))

print(binary)
