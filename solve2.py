from PIL import Image
import PIL.ImageOps
import qrtools

data = []
string_hasil = ""
for i in range(5103, 5120):
	namafile =  "0000"+str(i)+"inverted.png"
	namafile2 = "0000"+str(i)+"_1inverted.png"
	try:
		file = open(namafile, 'r')
		data.append(namafile)
	except:
		print "File Tak Ada"
	try:
		file = open(namafile2, 'r')
		data.append(namafile2)
	except:
		print "File Tak Ada"
#print string_hasil
print data

for i in data:
	qr = qrtools.QR()
	qr.decode(i)
	print qr.data
	string_hasil += qr.data
print string_hasil
