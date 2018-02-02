file_name = "play_play.txt"



# sentences are centered
with open(file_name) as file_object:
	for line in file_object:
		print(line.center(45))

# sentences are align right
with open(file_name) as file_object:
	for line in file_object:
		print(line.rjust(60))

# sentences are align left 
with open(file_name) as file_object:
	for line in file_object:
		print(line.ljust(60))
		