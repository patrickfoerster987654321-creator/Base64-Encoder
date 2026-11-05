def encode(in_file):
    file = open(in_file,'rb')
    out_file_name = f'{in_file}.txt'
    file2 = open(out_file_name, 'w')
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
        c1 = b64_alphabet[chunk1]
        c2 = b64_alphabet[chunk2]
        c3 = b64_alphabet[chunk3] if num_bytes > 1 else '='
        c4 = b64_alphabet[chunk4] if num_bytes > 2 else '='
        output = c1 + c2 + c3 + c4
        file2.write(output)

    



    file.close()
    file2.close()

    return out_file_name
