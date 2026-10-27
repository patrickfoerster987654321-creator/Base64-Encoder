Bitwise operators:
- | is bitwise or, it looks for a one and returns a one if there is one for that place in binary in either number (or both)
- & is bitwise and, it works the same as or but looks for 0 instead
- ^ is the xor operator, and it looks for difference and returns a 1 if bits are different for that place in binary and 0 if they aren't
- << is left shift, it takes a binary and shifts the numbers to the left by the number on the right, or exponentiates the binary
- >> is right shift, and it's the opposite of left shift, using floor division
- ~ is the not operator, and it flips the bits in a binary sequence, so 1s become 0s and vice versa, represented by -(x+1)

Bit representations:
- Binary, a base 2 system, the system that computers actually use. Ex: 0b0101 is 5 (1 in the fours place and 1 in the ones place)
- Octal, a base 8 system, takes binary and shrinks it down to make easier to manipulate. Ex: 0o22 is 18 (2 in the eighths place and 2 in the ones place)
- Hexadecimal, a base 16 system, the easiest for humans to read, the only one that uses letters, makes binary easier to manipulate. Ex: 0xFF is 255 (F is 15, so 15 in the sixteenths place and 15 in the ones place)

Bytes objects:
- Byte is a sequence of 8 bits. Ex: 11010100 is a byte.
- Python allows for the use of byte strings with the bytes data type
- It is declared with the b followed by a string, and returns the hex value as a number that represents each character using 7-bit ascii encoding. Ex b'Hi' returns 72 105 because that's there place in the ascii table
