import os
import sys

i = 1023
while(i>0):
	command1 = "unzip "+str(i)+".zip"
	print command1+"\n"
	os.system(command1)
	command2 = "rm "+str(i)+".zip"
	print command2+"\n"
	os.system(command2)
	command3 = "mv "+str(i)+"/"+str(i+1)+".zip"+" "+str(i+1)+".zip"
	print command3+"\n"
	os.system(command3)
	i -= 1
