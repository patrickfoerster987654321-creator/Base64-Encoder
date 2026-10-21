def encode(file):
    base64_chars = []
    file = open('file.bin','rb')
    while True:
        chunk = file.read(3)
        if not chunk:
            break

    file.close()
    file = open('file.txt', 'w')
