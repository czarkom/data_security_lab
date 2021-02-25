import multiprocessing
import time
import ctypes

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def xor64(a, b):
    block = bytearray(a)
    for j in range(8):
        block[j] = a[j] ^ b[j]
    return bytes(block)

def init(shared_data, output_data, block_size, key):
    multiprocessing.shared_data = shared_data
    multiprocessing.output_data = output_data
    multiprocessing.block_size = block_size
    multiprocessing.key = key


def mapper(blocks):
    cipher_text = multiprocessing.shared_data
    plain_text = multiprocessing.output_data
    block_size = multiprocessing.block_size
    des = DES.new(multiprocessing.key, DES.MODE_ECB)
    nonce = open("nonce", "rb").read()

    for i in blocks:
        offset = i * block_size
        block = cipher_text[offset:offset + block_size]
        count = nonce + i.to_bytes(4, byteorder="little")
        encrypted = des.encrypt(count)
        plain_text[offset:offset + block_size] = xor64(encrypted, block)
    return i


if __name__ == '__main__':
    key = b"haslo123"
    block_size = 8

    cipher_text = open("ciphertext", "rb").read()
    no_blocks = int(len(cipher_text) / block_size)
    W = [1,2,4]
    for w in W:
        shared_data = multiprocessing.RawArray(ctypes.c_ubyte, cipher_text)
        output_data = multiprocessing.RawArray(ctypes.c_ubyte, cipher_text)
        blocks = [range(i, no_blocks, w) for i in range(w)]
        # print(blocks)
        pool = multiprocessing.Pool(w, initializer=init, initargs=(shared_data, output_data, block_size, key))
        starttime = time.time()
        pool.map(mapper, blocks)
        print(f'CTR Decrypt time parallel for {w} workers: ', (time.time() - starttime))
        decrypted = bytes(output_data)
        print('...', decrypted[-15:-1])