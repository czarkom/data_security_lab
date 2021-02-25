import hashlib
import itertools
from time import perf_counter
import numpy as np

password = "fryta" #hasło dla którego mierzymy czas łamania brute forcem
h = hashlib.sha3_256(password.encode())
print("Hash:", h.hexdigest())

text_file = open("C:\\Users\\Maciej\\Downloads\\hashcat-6.1.1\\myhash.txt", "w") #ścieżka do pliku gdzie zapisujemy hash
text_file.write(h.hexdigest())
text_file.close()

t1_start = perf_counter()
from string import ascii_lowercase
alph = ascii_lowercase
keywords = itertools.product(alph, repeat=5)
hash_counter = 0
for i in keywords:
    key = ''
    for j in range(0, len(i)):
        key += i[j]
    h_try = hashlib.sha3_256(key.encode())
    hash_counter += 1
    if h.hexdigest() == h_try.hexdigest():
        print("Password cracked:", key)
        break
t1_stop = perf_counter()
time_elapsed = t1_stop - t1_start
max_hashes = np.power(26, 5)
speed = (hash_counter/time_elapsed)/1000
hashes_proceeded = (hash_counter/max_hashes)*100
print("Time elapsed [s]: ", time_elapsed)
print("Hashes proceeded:", hash_counter, '/', max_hashes)
print("Hashes proceeded (%):", hashes_proceeded, '%')
print("Speed:", speed, "kH/s")