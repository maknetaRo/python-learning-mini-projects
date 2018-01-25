
file_name = "play_play.txt"


with open(file_name) as file_object:
	for line in file_object:
		words = int(line.count(" ")) + 1
		print(line, words)


with open(file_name) as file_object:
	lines = file_object.readlines()

play_play = ""
for line in lines:
	play_play += line.strip()
	play_play = play_play.replace(".", " ")

words = int(play_play.count(" "))
print(play_play)
print("There are {} words.".format(words))

