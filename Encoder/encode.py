def encode(file:bytes):
    base64_chars = []
    for char in file:
        chunk = [i:i+3]

