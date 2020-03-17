file = open("YourPasswordHere", 'r')
data = file.read()


for i in range(0, 255):
	sit = ""
	for c in data:
		sit += chr(ord(c) ^ i)
	print sit
