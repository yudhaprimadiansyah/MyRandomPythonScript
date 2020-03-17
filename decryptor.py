import sys

file = open('yudhaencrypt.txt', 'r')
data = file.read()
file2 = open('yudhadecrypted.txt', 'w')
for i in data:
	decrypted = ord(i) + 5
	decryptedfix = chr(decrypted)
	file2.write(decryptedfix)
