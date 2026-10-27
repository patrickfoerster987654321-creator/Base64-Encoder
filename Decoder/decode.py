def decode(txt):
    file = open(f'{txt}', 'r')
    file2 = open('thing.png', 'w')
    b64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    while True:
        chunk = file.read(4)
        if not chunk:
            break
        chunk1 = (chunk.index(b64_alphabet) << 18) & 0x3F
        chunk2 = (chunk.index(b64_alphabet) << 12) & 0x3F
        chunk3 = (chunk.index(b64_alphabet) << 6) & 0x3F
        chunk4 = (chunk.index(b64_alphabet)) & 0x3F
        output = (
                chunk1,
                chunk2,
                chunk3
                )







    file.close()
    file2.close()
