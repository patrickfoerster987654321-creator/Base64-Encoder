def decode(txt):
    file = open(f'{txt}', 'r')
    encoded_data = file.read().replace('\n','').replace('\r','').strip()
    file2 = open('thing.png', 'wb')
    b64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    while True:
        indices = []
        i = 0
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
