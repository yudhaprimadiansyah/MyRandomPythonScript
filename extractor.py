import os

l = 1023
while True:
	executor2 = "tar jxvf "+str(l)+".tar.bz2"
	os.system(executor2)
	executor1 = "tar zxvf "+str(l)+".tar.gz"
	os.system(executor1)
	executor = "unzip "+str(l)+".zip"
	os.system(executor)
	executor3 = "mv "+str(l-1)+"/"+str(l-1)+".zip "+str(l-1)+".zip"
	os.system(executor3)
	executor31 = "mv "+str(l-1)+"/"+str(l-1)+".zip "+str(l-1)+".tar.gz"
	os.system(executor31)
	executor32 = "mv "+str(l-1)+"/"+str(l-1)+".zip "+str(l-1)+".tar.bz2"
	os.system(executor32)
	#executor3 = "mv "+str(l-1)+"/"+str(l-1)+".tar.gz "+str(l-1)+".zip"
	#os.system(executor3)
	#executor31 = "mv "+str(l-1)+"/"+str(l-1)+".tar.gz "+str(l-1)+".tar.gz"
	#os.system(executor31)
	#executor32 = "mv "+str(l-1)+"/"+str(l-1)+".tar.gz "+str(l-1)+".tar.bz2"
	#os.system(executor32)
	executor3 = "mv "+str(l-1)+"/"+str(l-1)+".tar.bz2 "+str(l-1)+".zip"
	os.system(executor3)
	executor31 = "mv "+str(l-1)+"/"+str(l-1)+".tar.bz2 "+str(l-1)+".tar.gz"
	os.system(executor31)
	executor32 = "mv "+str(l-1)+"/"+str(l-1)+".tar.bz2 "+str(l-1)+".tar.bz2"
	os.system(executor32)
	#executor2 = "rm "+str(l)+".zip"
	#os.system(executor2)
	#executor21 = "rm "+str(l)+".tar.gz"
	#os.system(executor21)
	#executor22 = "rm "+str(l)+".tar.bz2"
	#os.system(executor22)


	l -= 1
