file_name = "play_play.txt"

# first 
with open(file_name) as file_object:
	contents = file_object.read()
	print(contents)

# second
with open(file_name) as file_object:
	for line in file_object:
		print(line)

# third - making list
with open(file_name) as file_object:
	lines = file_object.readlines()

play_play = ""
for line in lines:
	play_play += line.rstrip()

print(play_play)
print(len(play_play))

# replace dog with cat
with open(file_name) as file_object:
	contents = file_object.read()
	print(contents.replace("dog", "cat"))

# check "is"
with open(file_name) as file_object:
	lines = file_object.readlines()

play_play = ""
for line in lines:
	play_play += line.rstrip()

word = "is"
if word in play_play:
	print(play_play.count("is"))
	print("There is 'is' in your file. ")
else:
	print("There is not any 'is' in your file.")
