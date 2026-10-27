def decode(txt):
    file = open(f'{txt}', 'r')
    encoded_data = file.read().replace('\n','').replace('\r','').strip()
    file2 = open('thing.png', 'wb')
    b64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    while True:
        indices = []
        i = 0
        while i < len(encoded_data):
            char = encoded_data[i]
            if char != '=':
                indices.append(b64_alphabet.index(char))
            i += 1
        file2.write(output)






    file.close()
    file2.close()
