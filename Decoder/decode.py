def decode(txt):
    file = open(f'{txt}', 'r')
    file2 = open('thing.png', 'w')
    b64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    while True:
        chunk = file.read(4)
        if not chunk:
            break
        chunk1 = (b64_alphabet.index(chunk) << 18) & 0x3F
        chunk2 = (b64_alphabet.index(chunk) << 12) & 0x3F
        chunk3 = (b64_alphabet.index(chunk) << 6) & 0x3F
        output = (
                chunk1,
                chunk2,
                chunk3
                )
        file2.write(output)






    file.close()
    file2.close()
