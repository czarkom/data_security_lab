import itertools
from Crypto.Cipher import ARC4
from string import ascii_lowercase
import sys
import math

text = "dupadupafajnajest"

cipher = ARC4.new('hejahola'.encode("utf-8"))
encrypted = cipher.encrypt(text.encode('utf-8'));
cipher = ARC4.new('hejahola'.encode("utf-8"))
decrypted = cipher.decrypt(encrypted);
print(encrypted)
print(decrypted)