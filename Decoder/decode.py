def decode(txt):
    file = open(f'{txt}', 'r')
    file2 = open('thing.png', 'w')
    b64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

