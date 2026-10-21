def encode(file):
    base64_chars = []
    for char,item in enumerate(file):
        if item % 3 == 0:
            chunk = item[:3]

