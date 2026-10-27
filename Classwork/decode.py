def decode(nums):
    """
      >>> decode([22, 53, 44, 19, 63, 15])
      'W1sT/P'
      >>> decode([0, 1, 2, 3, 4, 5, 6])
      'ABCDEFG'
      >>> decode([26, 27, 28, 29, 30, 31, 32])
      'abcdefg'
      >>> decode([53, 54, 55, 56, 57])
      '12345'
    """
    b64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    b64_str = ''
    for item in nums:
        b64_str += b64_alphabet[item]
        
    return b64_str


if __name__ == '__main__':
    import doctest
    doctest.testmod()
