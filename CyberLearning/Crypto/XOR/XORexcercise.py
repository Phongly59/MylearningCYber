from Crypto.Util.number import long_to_bytes

# Định nghĩa các khóa dưới dạng hex
KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_XOR_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_XOR_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_XOR_KEYS = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# Chuyển đổi từ hex sang int
key1_int = int(KEY1, 16)
key2_xor_key1_int = int(KEY2_XOR_KEY1, 16)
key2_xor_key3_int = int(KEY2_XOR_KEY3, 16)
flag_xor_keys_int = int(FLAG_XOR_KEYS, 16)

# Tính toán KEY2
KEY2 = key1_int ^ key2_xor_key1_int
print("KEY2 (int):", KEY2)

# Tính toán KEY3
KEY3 = KEY2 ^ key2_xor_key3_int
print("KEY3 (int):", KEY3)

# Tính toán FLAG
FLAG = flag_xor_keys_int ^ key1_int ^ KEY2 ^ KEY3
print("FLAG (int):", FLAG)

# Chuyển đổi FLAG sang bytes
flag_bytes = long_to_bytes(FLAG)
print(flag_bytes)

# Chuyển đổi bytes thành chuỗi
flag_string = flag_bytes.decode('utf-8', errors='ignore')
print("FLAG (string):", flag_string)

# Định dạng kết quả
formatted_flag = f"crypto{{{flag_string}}}"
print("Formatted FLAG:", formatted_flag)
