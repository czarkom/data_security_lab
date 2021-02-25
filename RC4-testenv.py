import itertools
from Crypto.Cipher import ARC4
from string import ascii_lowercase
import sys
import math

ARC4.key_size = range(3, 257)
alph = ascii_lowercase
keywords = itertools.product(alph, repeat=3)

#podajemy plik jako argument przy wywołaniu programu, w naszym przypadku będzie to plik RC4.py
f = open(sys.argv[1],'rb')
d = f.read()

dict = {}

for i in keywords:
    key = i[0]+i[1]+i[2]
    cipher = ARC4.new(key.encode("utf-8"))
    decrypted = cipher.decrypt(d)
    stat = {}
    for c in decrypted:
        m = c
        if m in stat:
            stat[m] += 1
        else:
            stat[m] = 1
    H = 0.0
    for i in stat.keys():
        pi = stat[i] / len(d)
        H -= pi * math.log2(pi)
    dict[key] = H
print("Key found by bruteforce is " + min(dict, key=dict.get))
#Otrzymany klucz to "def", możemy teraz odczytać rozszyfrowany tekst
cipher = ARC4.new(min(dict, key=dict.get).encode("utf-8"))
decrypted = cipher.decrypt(d)
print(decrypted)
