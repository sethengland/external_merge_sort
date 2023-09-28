import struct

def verify_is_sorted(filename, M):
    file = open(filename, 'rb')
    prev = None
    while True:
        chunk = file.read(M * 4)
        if not chunk:
            break
        data = list(struct.unpack('I' * (len(chunk) // 4), chunk))
        for integer in data:
            if prev is not None and prev > integer:
                return False
            prev = integer
    return True