def base64_to_bits(b64str):
    """
      >>> base64_to_bits('R0hn')
      '010001110100100001100111'
      >>> base64_to_bits('VGVz')
      '010101000110010101110011'
      >>> base64_to_bits('TQ==')
      '01001101'
      >>> base64_to_bits('TWE=')
      '0100110101100001'
      >>> base64_to_bits('nWlTXneO1zD')
      '1001110101101001010100110101111001110111100011101101011100110000'
      >>> s2 = '10110101100010110011010101010110111100011101101011100101'
      >>> base64_to_bits('tYs1VvHa5Q==') == s2
      True
    """
    bit_str = ''
    b64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    for char in b64str:
        if char == '=':
            continue


        if char in b64_alphabet:
            val = b64_alphabet.index(char)
            bit_str += bin(val)[2:].zfill(6)


    if len(bit_str) % 8 != 0:
        bit_str = bit_str[:-(len(bit_str) % 8)]

    return bit_str




if __name__ == '__main__':
    import doctest
    doctest.testmod()
