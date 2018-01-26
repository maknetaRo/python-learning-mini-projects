import random

print("This is a random gift sugestion")
print("Choose who is the gift for: ")
print("Enter: (Judyta, Mateusz, Jedrzej, Mariusz) ")
name = input()

judyta = ["cat's T-shirt", "purse", "handbag", "tablet case", "rollerskates", "mobile phone",
 "guitar", "fancy journal", "ukulele", "skate padset", "hair accessories"]

mateusz = ["wallet", "sweatshirt", "kindle case", "xxl mug", "new J.K.Rowling's book"]

jedrzej = ["wallet", "jacket", "hand blender", "leather belt", "dressing-gown", "infinity scarf"]

mariusz = ["dartboard", "steel darts set", "training gloves", "astronomy book"]

if name == "Judyta":
	print(random.choice(judyta))
elif name == "Mateusz":
	print(random.choice(mateusz))
elif name == "Jedrzej":
	print(random.choice(jedrzej))
elif name == "Mariusz":
	print(random.choice(mariusz))
else:
	print("Ups, something went wrong.")