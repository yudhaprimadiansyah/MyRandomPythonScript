import struct
import sys
import base64

#if len(sys.argv) != 2:
#	print "Usage: %s data" % sys.argv[0]
#	exit(0)

data = open('cipher3.txt', 'r').read().rstrip() #sys.argv[1]
#padding = 4 - len(data) % 4
#if padding != 0:
#	data = data + "\x00" * padding

result = []
blocks = struct.unpack("I" * (len(data) / 4), data)
for block in blocks:
	result += [block ^ block << 16]
	print str(block) +" : "+ str([block ^ block >> 16])

print result

output = ''
for block in result:
	output += struct.pack(">I", block)
	print str(block) + " : " + struct.pack("I", block)
print base64.b64encode(output)

