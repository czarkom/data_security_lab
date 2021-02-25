from Crypto.Cipher import DES,AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import BMPencrypt
from photo_ent import photo_ent
from string import ascii_lowercase
import itertools
import os

#klucz 128 bit powstał z wykorzystaniem PBKDF2(b"[a-z]{3}, b"abc") iv=16*a

alph = ascii_lowercase
keywords = itertools.product(alph, repeat=3)

# iv = "a"*16
# salt = b"abc"

dict = {}
for i in keywords:
    password = i[0]+i[1]+i[2]
    # password = PBKDF2(i.encode("utf-8"), salt)
    filename = BMPencrypt.decrypt('we800_CBC_encrypted.bmp', password)
    dict[password] = photo_ent(filename)
    os.remove(filename)
    print(password)
solution = min(dict, key=dict.get)
print("Key found by bruteforce is " + solution)
filename = BMPencrypt.decrypt('we800_CBC_encrypted.bmp', solution)

# des = DES.new("key12345".encode("utf-8"), DES.MODE_CBC, iv)
# encrypted = des.encrypt(b"secret12")
# print(encrypted)
# des = DES.new("key12345".encode("utf-8"), DES.MODE_CBC, iv)
# print(des.decrypt(encrypted))

# BMPencrypt.encrypt("demo24.bmp", "CBC", key)