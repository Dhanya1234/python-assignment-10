with open("samplef.txt")as f:
	data=f.read()
	print(data)
	f=open("sample.txt")
	f.write("hello dhanya")
	print(f.read)