def encode(file):
    base64_chars = []
    file = open(file,'rb')
    while True:
        chunk = file.read(3)
        if not chunk:
            break
        chunk_int = int.from_bytes(chunk, 'big')

    file.close()
    file2 = open('file.txt', 'w')
    chunk1 = (chunk_int >> 18) & 0x3F
    chunk2 = (chunk_int >> 12) & 0x3F
    chunk3 = (chunk_int >> 6) & 0x3F
    chunk4 = chunk_int & 0x3F
    output = (
            chunk1,
            chunk2,
            chunk3,
            chunk4
            )
    file2.write(output)
    file2.close()
