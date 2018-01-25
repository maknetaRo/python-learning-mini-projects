
file_name = "play_play.txt"


with open(file_name) as file_object:
	for line in file_object:
		words = line.split()
		number = len(words)
		print(line, words, number)


with open(file_name) as file_object:
	lines = file_object.readlines()

play_play = ""
for line in lines:
	play_play += line.strip()
	play_play = play_play.replace(".", " ")

words = play_play.spli()
number = len(words)
print(play_play)
print("There are {} words.".format(number))

infile = open("C:\\Users\\Magda\\Desktop\\simple\\learning_python.txt", "r")
data = infile.read()
num_of_chars = len(data)
num_of_words = len(data.split())
num_of_lines = len(data.splitlines())

print(num_of_chars, num_of_words, num_of_lines)


