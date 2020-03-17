file = open('soal3_2.stack')
data = file.read()

gg = 0
new = ""
for i in range(0, len(data)-2, 2):
	new += data[i]
file = open('jadi.jpg', 'w')
file.write(new)
file.close()
