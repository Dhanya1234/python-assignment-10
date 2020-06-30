with open ("sample.txt")as f:
	data=f.readlines
	for line in data:
		sentence=line.split()
		print(sentence)