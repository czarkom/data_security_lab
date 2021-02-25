from Crypto.Cipher import DES,AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

print(PBKDF2(b"password", b"salt"))

#des = DES.new("key12345")
iv = get_random_bytes(8)
des = DES.new("key12345".encode("utf-8"),DES.MODE_CBC, iv)
encrypted = des.encrypt("secret12".encode("utf-8"))
print(encrypted)
iv = get_random_bytes(16)
aes = AES.new(b"key1234578901238", AES.MODE_CFB, iv)
encrypted = aes.encrypt("tesł".encode("utf-8"))
print(encrypted)