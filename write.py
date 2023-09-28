import random
import struct

def write_integers(filename, N):
    file = open(filename, 'wb')
    for i in range(N):
        out = random.randint(0, (2 ** 32) - 1)
        file.write(struct.pack("I", out))
    file.close()

