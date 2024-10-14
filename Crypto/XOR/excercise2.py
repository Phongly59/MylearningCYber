# Function to decrypt using XOR
def xor_decrypt(byte_array, key):
    key_length = len(key)
    decrypted = bytearray()
    for i in range(len(byte_array)):
        decrypted.append(byte_array[i] ^ key[i % key_length])  # Repeat key as needed
    return decrypted

# Known flag starting characters for "crypto{"
known_flag = b'crypto{'
byte_array = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

# Extract the first seven bytes of the byte array
extracted_bytes = byte_array[:len(known_flag)]

# Calculate possible key bytes
possible_key = []
for i in range(len(known_flag)):
    key_byte = extracted_bytes[i] ^ known_flag[i]
    possible_key.append(key_byte)

# Convert the new possible key back to bytes
new_key_bytes = bytes(possible_key)

# Decrypt the byte array using the new key
decrypted_bytes = xor_decrypt(byte_array, new_key_bytes)

# Print the decrypted result
print("Decrypted bytes:", decrypted_bytes)
print("Decrypted text:", decrypted_bytes.decode('latin1', errors='ignore'))  # Using latin1 to handle non-ASCII


