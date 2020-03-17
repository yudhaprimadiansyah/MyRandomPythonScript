# Pada Suatu Hari, Wik_Wik dikirimi pesan oleh seseorang dari klub pecinta serangga, namun pesan tersebut terenskripsi, orang tersebut hanya
# memberikan Kunci dan sebuah potongan kode program yang menurutnya akan sangat berguna, kunci yang diberikan yaitu = PECINTASERANGGA
# coba bantu Wik_Wik memecahkan kodenya
def encrypt(text,key):
	cipher = ""
	d = 0
	for i in range(0, len(text)):
		cipher += chr(ord(text[i]) + ord(key[d]))
		if d == len(key)-1:
			d = 0
		else:
			d+=1
	return cipher
