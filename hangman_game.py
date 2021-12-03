def read():
	with open("./words.txt", "r", encoding= "utf-8") as f:
		for line in f:
			words.append(line)

def run():
	words = []
	print(words)


if __name__ == "__main__":
	run()
