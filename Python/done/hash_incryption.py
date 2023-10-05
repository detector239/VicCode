import hashlib

hsh = hashlib.new('blake2b')
hsh.update('asdfgh1!'.encode())

print(b'asdfgh1!')

print(hsh.digest())
