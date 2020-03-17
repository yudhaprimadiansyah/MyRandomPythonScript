file = open('final', 'r')
data = file.read();
hasil = ""
file2 = open('biner', 'w')

for i in data:
	if i == '1' or i == '0':
		hasil += i
	else:
		continue

file2.write(hasil)
file2.close()
