import hashlib

with open("test.txt","rb") as f:
    h = hashlib.sha3_256(f.read())
    print(h.hexdigest())

