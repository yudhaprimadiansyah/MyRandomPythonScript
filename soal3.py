file = open('soal3.png', 'r')
data = file.read()
i = 0
newdat = ""
for i in data:
	if(i == (i-1)):
		continue
	else:
		newdat += i
#while True:
#	newdat += data[i]
#	i += 2
print newdat


