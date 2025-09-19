def hex_xor(a: str, b: str) -> str:
    """XOR two equal-length hex strings and return hex string (lowercase, without 0x)."""
    a_bytes = bytes.fromhex(a)
    b_bytes = bytes.fromhex(b)
    return bytes(x ^ y for x, y in zip(a_bytes, b_bytes)).hex()

KEY1       = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
K2_xor_K1  = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
K2_xor_K3  = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FINAL      = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"  # FLAG ^ KEY1 ^ KEY3 ^ KEY2

# Recover keys
KEY2 = hex_xor(K2_xor_K1, KEY1)       # KEY2 = (KEY2 ^ KEY1) ^ KEY1
KEY3 = hex_xor(KEY2, K2_xor_K3)       # KEY3 = (KEY2 ^ KEY3) ^ KEY2

# Recover FLAG: FINAL = FLAG ^ KEY1 ^ KEY3 ^ KEY2  -> FLAG = FINAL ^ KEY1 ^ KEY3 ^ KEY2
temp = hex_xor(KEY1, KEY3)
temp = hex_xor(temp, KEY2)
FLAG_hex = hex_xor(FINAL, temp)

flag = bytes.fromhex(FLAG_hex).decode()
print("FLAG:", flag)
# output: crypto{x0r_i5_ass0c1at1v3}
