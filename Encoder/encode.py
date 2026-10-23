def encode(file):
    base64_chars = []
    file = open(file,'rb')
    while True:
        chunk = file.read(3)
        if not chunk:
            break

    file.close()
    file2 = open('file.txt', 'w')
    chunk1 = (chunk >> 18) & 0x3F
    chunk2 = (chunk >> 12) & 0x3F
    chunk3 = (chunk >> 6) & 0x3F
    chunk4 = chunk & 0x3F
    output = (
            chunk[chunk1],
            chunk[chunk2],
            chunk[chunk3],
            chunk[chunk4]
            )
    file2.write(output)
    file2.close()
