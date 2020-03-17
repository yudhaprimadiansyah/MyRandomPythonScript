from PIL import Image
import os
import hashlib
import shutil

def crack(filename):
	for i in range(0, 600):
		hash = filename[:-4]
		#print hash
		if(hashlib.md5(str(i)).hexdigest() == hash):
			print "[+] Hash Ketemu {} : {}".format(i, filename)
			src = filename
			print filename
			print os.listdir
			dest = str(i)+".png"
			#shutil.copyfile(src,dest)
			os.rename(src, dest)

im = Image.new('RGB', (600, 267))

data = os.listdir('.')
data.remove('solve.py')
#print sorted(data)
#for datas in data:
#	crack(datas)
offset = 0
for i in range(0, 600):
	if str(i)+".png" in data:
		gbr = Image.open(str(i)+'.png')
		print offset
		im.paste(gbr, (offset, 0))
		offset += gbr.size[0]

im.save('baru.png')
