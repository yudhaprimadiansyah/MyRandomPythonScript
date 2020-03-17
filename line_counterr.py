import os

total = 0
while True:
	print "List File : "
	os.system('ls')
	namafile = raw_input("Masukan Nama File = ").rstrip()
	try:
		file = open(namafile, 'rw')
		data = file.read()
	except:
		print "File Tidak Ada"
		continue
	for i in data:
		if hex(ord(i)) == hex(ord("\n")):
			total += 1
		else:
			continue
	file.close()
	print "\n\nTotal Baris = ", total

