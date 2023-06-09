import sys

def rotate_left(value, rotation):
    # Rotate the bits of 'value' to the left by 'rotation' positions
    return ((value << rotation) | (value >> (64 - rotation))) & 0xFFFFFFFFFFFFFFFF

def mix(key, tweak):
    # Mix the key and tweak values using a series of operations
    key[0] += key[1]  # Add key[1] to key[0]
    key[1] = rotate_left(key[1], 14)  # Rotate key[1] to the left by 14 positions
    key[1] ^= key[0]  # Bitwise XOR of key[1] with key[0]

    key[2] += key[3]  # Add key[3] to key[2]
    key[3] = rotate_left(key[3], 16)  # Rotate key[3] to the left by 16 positions
    key[3] ^= key[2]  # Bitwise XOR of key[3] with key[2]

    key[0] += key[3]  # Add key[3] to key[0]
    key[3] = rotate_left(key[3], 52)  # Rotate key[3] to the left by 52 positions
    key[3] ^= key[0]  # Bitwise XOR of key[3] with key[0]

    key[2] += key[1]  # Add key[1] to key[2]
    key[1] = rotate_left(key[1], 57)  # Rotate key[1] to the left by 57 positions
    key[1] ^= key[2]  # Bitwise XOR of key[1] with key[2]

    key[0] += key[1]  # Add key[1] to key[0]
    key[1] = rotate_left(key[1], 23)  # Rotate key[1] to the left by 23 positions
    key[1] ^= key[0]  # Bitwise XOR of key[1] with key[0]

    key[2] += key[3]  # Add key[3] to key[2]
    key[3] = rotate_left(key[3], 40)  # Rotate key[3] to the left by 40 positions
    key[3] ^= key[2]  # Bitwise XOR of key[3] with key[2]

    key[0] += key[3]  # Add key[3] to key[0]
    key[3] = rotate_left(key[3], 5)  # Rotate key[3] to the left by 5 positions
    key[3] ^= key[0]  # Bitwise XOR of key[3] with key[0]

    key[2] += key[1]  # Add key[1] to key[2]
    key[1] = rotate_left(key[1], 37)  # Rotate key[1] to the left by 37 positions
    key[1] ^= key[2]  # Bitwise XOR of key[1] with key[2]

    return key

def to_bytes(num, byteorder='big'):
    # Convert an integer 'num' to a bytes object with specified byte order
    length = (num.bit_length() + 7) // 8
    return int.to_bytes(num, length, byteorder)

def encrypt_password(password, key):
    if len(password) % 64 != 0:
        password += '\x00' * (64 - (len(password) % 64))
    # Pad the password with null bytes if its length is not a multiple of 64

    blocks = [password[i:i+64] for i in range(0, len(password), 64)]
    # Divide the password into blocks of 64 characters

    for block in blocks:
        block_words = [int.from_bytes(block[i:i+8].encode(), sys.byteorder) for i in range(0, len(block), 8)]
        # Convert each 8-byte segment of the block to integers

        block_words = mix(block_words + key, key + block_words)
        # Mix the block words with the key and tweak

        block_bytes = b''.join(to_bytes(word) for word in block_words)
        # Convert the block words back to bytes and join them together

        print(block_bytes)
        # Print the encrypted block bytes

password = "password"
key = [0x0123456789ABCDEF, 0x89ABCDEF01234567, 0xFEDCBA9876543210, 0x76543210FEDCBA98]
encrypt_password(password, key)
