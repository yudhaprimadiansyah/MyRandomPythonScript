import string

key = 'SISFOTIME2019'
#key = "AB"

def encrypt(what):
	encrypted = ''
	lens = ''
	#assert len(what) > len(key)
	for r in xrange(len(what)):
		print r
		tmp = str((ord(what[r]) ^ ord(key[r % len(key)])) << 1337)
		print "tmp : "+tmp
		lens += str(len(tmp) ^ 1337)
		print "Lens : "+lens
		print "lentmp : "+str(len(tmp))
		encrypted += tmp
	return ['{} messages encrypted'.format(len(what)), '{}{}{}'.format(encrypted, lens, str(len(what)).zfill(5))]


baru = []
def decrypt(naon, keyk):
	leng = int(naon[-5:len(naon)])
	key = int(naon[-(5+(4*leng)):len(naon)-5])
	encrypted = int(naon[0:len(naon)-(5+(4*leng))])
	enc_str = str(encrypted)
	keynya = str(key)
	keys = [keynya[i:i+4] for i in range(0, len(keynya), 4)]
	tiap_karakter = []
	for a in keys:
		c = int(a) ^ 1337
		if(c == 1):
			tiap_karakter.append('0')
			enc_str = enc_str[c:]
		else:
			tiap_karakter.append(enc_str[0:c])
			enc_str = enc_str[c:]
	index_key = 0
	hasil = ""
	for j in tiap_karakter:
		print keyk[index_key]+" : "+str(ord(keyk[index_key]))
		print "Encrypted : "+str(j)
		kunci = (int(j) ^ ord(keyk[index_key])) >> 1337
		print "Kunci : "+str(kunci)
		print "hasil : "+chr(ord(keyk[index_key]) ^ kunci)
		hasil += chr(ord(keyk[index_key]) ^ kunci)
		index_key += 1
		if index_key >= len(keyk):
			index_key = 0
		print hasil
#	decrypted = ''
#	panyang = ''
#	haha = (len(naon)-5)/int(naon[-3:len(naon)])
#	for i in range(1, ((len(naon))/haha)):
#		dekrep = naon[(haha*(i-1)):(haha*i)]
#		baru.append(dekrep)
#		print haha*i
#	return ["{} pembagian dari panjang teks/len asli".format(haha), "{} len asli teks".format(len(naon)-5), "{} ini dari lengthnya".format((len(naon)-5)/haha)]
	return "{}".format(hasil)

file = open('encrypted', 'r')
data = file.read()
#data = "NAMA SAYA YUDHA PRIMADIANSYAH"
#data = "SISFOTIME2019"
#data = "AAA"
#encipt = encrypt(data)
decipt = decrypt(data, key)
#decipt = decrypt(data, key)
#print encipt
print decipt
#print baru
#print decrypt(data)
#*with open('secret', 'rb') as secret:
#    secret_file = ''.join(secret.readlines())
#
#assert len(key) == 13
#assert 'Sisfotime' in secret_file
#for i in secret_file:
#    if i not in string.ascii_letters + '{}_?!,. ':
#        print 'Invalid Secret'
#        exit()

#cipher = encrypt(secret_file)
#print cipher[0]

#with open('encrypted', 'w+') as enc:
#    enc.write(cipher[1])
#    enc.close()

