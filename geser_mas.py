import string

key = 'SISFOTIME2019'


def encrypt(what):
    encrypted = ''
    lens = ''
    assert len(what) > len(key)
    for r in xrange(len(what)):
        tmp = str((ord(what[r]) ^ ord(key[r % len(key)])) << 1337)
        lens += str(len(tmp) ^ 1337)
        encrypted += tmp
    return ['{} messages encrypted'.format(len(what)), '{}{}{}'.format(encrypted, lens, str(len(what)).zfill(5))]


with open('secret', 'rb') as secret:
    secret_file = ''.join(secret.readlines())

assert len(key) == 13
assert 'Sisfotime' in secret_file
for i in secret_file:
    if i not in string.ascii_letters + '{}_?!,. ':
        print 'Invalid Secret'
        exit()

cipher = encrypt(secret_file)
print cipher[0]

with open('encrypted', 'w+') as enc:
    enc.write(cipher[1])
    enc.close()
