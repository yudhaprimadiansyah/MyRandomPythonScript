import struct

data = open('cipher3.txt', 'r').read().rstrip()

result = ""
for block in data:
	print block
	result += struct.pack(">I", ord(block))
print result
