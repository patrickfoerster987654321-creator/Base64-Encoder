def bits_to_base64(bitstr):
    """
      >>> bits_to_base64('010001110100100001100111')
      'R0hn'
      >>> bits_to_base64('010101000110010101110011')
      'VGVz'
      >>> bits_to_base64('01001101')
      'TQ=='
      >>> bits_to_base64('0100110101100001')
      'TWE='
      >>> s = '100111010110100101010011010111100111011110001110110101110011011'
      >>> result = bits_to_base64(s)
      >>> result
      'nWlTXneO1zD'
      >>> s2 = '10110101100010110011010101010110111100011101101011100101'
      >>> result2 = bits_to_base64(s2)
      >>> result2
      'tYs1VvHa5Q=='
    """
    ret = ""
    b64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    remainder = len(bitstr) % 6
    if remainder != 0:
        padding = 6 - remainder
        bitstr += '0' * padding
    else:
        padding = 0


    for index in range(0, len(bitstr), 6):
        s = bitstr[index:(index+6)]
        val = int(s, 2)
        ret += b64_alphabet[val]

    if padding == 2:
        ret += '='
    elif padding == 4:
        ret += '=='

    return ret



if __name__ == '__main__':
    import doctest
    doctest.testmod()
