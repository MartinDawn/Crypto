# single_byte_xor.py
cipher_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
cipher = bytes.fromhex(cipher_hex)

for key in range(256):
    plain = ''.join(chr(c ^ key) for c in cipher)
    if plain.startswith("crypto{"):   # flag dạng crypto{...}
        print("Key:", key)
        print("Flag:", plain)
        break
# output:  crypto{0x10_15_my_f4v0ur173_by7e}