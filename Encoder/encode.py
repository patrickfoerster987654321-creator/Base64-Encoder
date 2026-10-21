def encode(file):
    base64_chars = []
    file = open('file.bin','rb')
    while True:
        chunk = file.read(3)
        if not chunk:
            break

    file.close()
    file = open('file.txt', 'w')
    chunk1 = (chunk >> 18) & 0x3F
    chunk2 = (chunk >> 12) & 0x3F
    chunk3 = (chunk >> 6) & 0x3F
    chunk4 = chunk & 0x3F
