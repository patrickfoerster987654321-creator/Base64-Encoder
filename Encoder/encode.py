def encode(file):
    base64_chars = []
    file = open(file,'rb')
    file2 = open('file.txt', 'a', encoding = 'ascii')
    b64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    while True:
        chunk = file.read(3)
        if not chunk:
            break
        num_bytes = len(chunk)
        padded_chunk = chunk + b'\x00' * (3-num_bytes)
        chunk_int = int.from_bytes(padded_chunk, 'big')
        chunk1 = (chunk_int >> 18) & 0x3F
        chunk2 = (chunk_int >> 12) & 0x3F
        chunk3 = (chunk_int >> 6) & 0x3F
        chunk4 = chunk_int & 0x3F
        output = (
            b64_alphabet[chunk1] +
            b64_alphabet[chunk2] +
            b64_alphabet[chunk3] +
            b64_alphabet[chunk4]
            )
        file2.write(output)

    



    file.close()
    file2.close()
