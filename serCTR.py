import multiprocessing
import time
import ctypes

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# zakłada, że a i b są bytes
def xor64(a, b):
    block = bytearray(a)
    for j in range(8):
        block[j] = a[j] ^ b[j]
    return bytes(block)

# zakłada, że key i plain_text są bytes
def encrypt_CTR_serial(key, plain_text, nonce):
    cipher_text = bytearray(plain_text) # kopia! bytes -> bytearray
    des = DES.new(key, DES.MODE_ECB)
    for i in range(no_blocks):
        offset = i*block_size
        block = plain_text[offset:offset+block_size]
        count = nonce + i.to_bytes(4, byteorder="little")
        encrypted = des.encrypt(count)
        cipher_text[offset:offset+block_size] = xor64(encrypted, block)
    return bytes(cipher_text) # bytearray -> bytes

# zakłada, że key i cipher_text są bytes
def decrypt_CTR_serial(key, cipher_text, nonce):
    plain_text = bytearray(cipher_text)
    des = DES.new(key, DES.MODE_ECB)
    for i in range(no_blocks):
        offset = i*block_size
        block = cipher_text[offset:offset+block_size]
        count = nonce + i.to_bytes(4, byteorder="little")
        encrypted = des.encrypt(count)
        plain_text[offset:offset+block_size] = xor64(encrypted, block)
    return bytes(plain_text)

plain_text = b"maciejczarkowski"*100000
key = b"haslo123"
nonce = get_random_bytes(4)
block_size = 8
no_blocks = int(len(plain_text)/block_size)

starttime = time.time()
cipher_text = encrypt_CTR_serial(key, plain_text, nonce)
print('CTR Encrypt time serial: ', (time.time() - starttime))

starttime = time.time()
decrypted = decrypt_CTR_serial(key, cipher_text, nonce)
print('CTR Decrypt time serial: ', (time.time() - starttime))
print('...', decrypted[-15:-1])

with open('ciphertext', 'wb') as f:
	f.write(cipher_text)

with open('nonce', 'wb') as f:
	f.write(nonce)