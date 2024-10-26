def xor_with_key(data, key):
    return bytes(b ^ key for b in data)

def is_readable(text):
    return all(32 <= b < 127 for b in text)

hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
bytes_data = bytes.fromhex(hex_string)

for key in range(256):
    decrypted = xor_with_key(bytes_data, key)
    if is_readable(decrypted):
        print(f"Key: {key}, Decrypted: {decrypted.decode('utf-8')}")
