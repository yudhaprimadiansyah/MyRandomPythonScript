
file = open("payload.py", 'w')
data = ""
string = "0123456789ABCDEF"
payload = ""
for i in string:
	for a in string:
		payload += "(('"+a+"'*3)+('"+i+"'*4)+'\\x"+i+a+"')+"
file.write(payload)
file.close()
