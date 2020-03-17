from PIL import Image
import qrtools
data = []
for i in range(1,625):
	namgam = "um_"+str(i)+".jpg"
	im = Image.open(namgam)
	pic = im.load()
	data.append(pic[1,1])
	
gambar = Image.new('RGB', (25,25))
gambar.putdata(data)
gambar.save('yuyud.png')

qr = qrtools.QR()
qr.decode('yuyud.png')
print qr.data
