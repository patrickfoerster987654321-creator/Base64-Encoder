def decode(txt):
    file = open(f'{txt}', 'r')
    encoded_data = file.read().replace('\n','').replace('\r','').strip()
    file2 = open('thing.png', 'wb')
    b64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    indices = []
    padding_count = '='
    for char in encoded_data:
        char = encoded_data[i]
        if char != '=':
            indices.append(b64_alphabet.index(char))
        i += 1
    byte_list = bytearray()
    index = 0
    while index < len(indices):
        b1 = indices[index]
        b2 = indices[index + 1]
        b3 = indices[index + 2]
        b4 = indices[index + 3]

    triple = (b1 << 18) + (b2 << 12) + (b3 << 6) + b4
    byte_list.append((triple >> 16) & 0xFF)
    if index + 2 < len(indices):
        byte_list.append((triple >> 8) & 0xFF)
    if index + 3 < len(indices):
        byte_list.append(triple & 0xFF)


    index += 4
    file2.write(bytes(byte_list))






    file.close()
    file2.close()
