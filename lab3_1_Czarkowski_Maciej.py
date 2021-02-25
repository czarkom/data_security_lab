#Maciej Czarkowski
#Wynik to "fed", na obrazku pokazuje się logo Wydziału Elektrycznego
from string import ascii_lowercase
import itertools
import os
from math import log2
from PIL import Image
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2


def photo_ent(file):
    counts = [0] * 256
    with open(file, 'rb') as f:
        for c in f.read():
            if c < 255:
                counts[c] += 1
    l = sum(counts)
    p = [c/l for c in counts]
    h = -sum([pi*log2(pi) for pi in p if pi > 0.0])
    return h


def expand_data(data):
    return data + b"\x00"*(16-len(data)%16)


def convert_to_rgb(data):
    pixels = []
    counter = 2
    for i in range(len(data)-1):
        if counter == 2:
            r = int(data[i])
            g = int(data[i+1])
            b = int(data[i+2])

            pixels.append((r,g,b))
            counter = 0
        else:
            counter += 1
    return pixels


def decrypt(input_filename, password):
    img_in = Image.open(input_filename)
    data = img_in.convert("RGB").tobytes()
    data_expanded = expand_data(data)
    iv = b"a"*16
    salt = b"abc"
    key = PBKDF2(password.encode(), salt)
    aes = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = convert_to_rgb(aes.decrypt(data_expanded)[:len(data)])
    img_out = Image.new(img_in.mode, img_in.size)
    img_out.putdata(encrypted_data)
    name = ''.join(input_filename.split('.')[:-1])
    img_format = str(input_filename.split('.')[-1])
    output_filename = name + '_' + password + '_decrypted.' + img_format
    img_out.save(output_filename, img_format)
    return output_filename


#klucz 128 bit powstał z wykorzystaniem PBKDF2(b"[a-z]{3}, b"abc") iv=16*a

alph = ascii_lowercase
keywords = itertools.product(alph, repeat=3)

dict = {}
for i in keywords:
    password = i[0]+i[1]+i[2]
    filename = decrypt('we800_CBC_encrypted.bmp', password)
    dict[password] = photo_ent(filename)
    os.remove(filename)
    print(password)
solution = min(dict, key=dict.get)
print("Key found by bruteforce is " + solution)
filename = decrypt('we800_CBC_encrypted.bmp', solution)

#Otrzymane hasło to "fed". Wynikiem jest logo Wydziału Elektrycznego PW