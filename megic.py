file = open('megic.png', 'r').read()

for i in range(0,255):
	new_str = ""
	for j in file:
		new_str += chr(ord(j) ^ i)
	if("P" in new_str == True):
		print "ada di "+str(i)
	else:
		continue
	print new_str		
