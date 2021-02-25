from sys import argv
from math import log2
import matplotlib.pyplot as plt


def photo_ent(file):
    counts = [0]*256
    with open(file, 'rb') as f:
        for c in f.read():
            if c < 255:
                counts[c] += 1
    # print(counts)
    l = sum(counts)
    p = [c/l for c in counts]
    h = -sum([pi*log2(pi) for pi in p if pi > 0.0])
    # print(f"Entropia pliku to {H}")

    # plt.bar(range(256), counts)
    # plt.show()
    return h