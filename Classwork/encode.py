def encode(s):
    """
      >>> encode("W1sT/P")
      [22, 53, 44, 19, 63, 15]
      >>> encode("ABCDEFG")
      [0, 1, 2, 3, 4, 5, 6, 7]
      >>> encode("abcdefg")
      [26, 27, 28, 29, 30, 31, 32]
      >>> encode("12345")
      [53, 54, 55, 56, 57]
    """
    b64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    for char in s:

