def decode(txt):
    file = open(f'{txt}', 'r')
    file2 = open('thing.png', 'w')
    b64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    while True:
        chunk = file.readline()
        if not chunk:
            break
        chunk = b64_alphabet.index(chunk)
        output = (
                chunk
                )
        file2.write(output)






    file.close()
    file2.close()
