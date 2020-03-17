import os
import sys


file = open('soal3.jpg', 'r')
data = file.read()
file2 = open('soal3_2.jpg', 'w')
data2 = ""
for i in range(1, len(data), 2):
	data2 += data[i]

file2.write(data2)
file2.close()
