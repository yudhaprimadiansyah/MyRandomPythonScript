cipher = "a)))KkFmQ*wFz)TixK*||"

plain = ""
for j in cipher:
	plain += chr(ord(j) ^ 0x19)
print plain
