from binascii import unhexlify
cipher = unhexlify("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

known = b"crypto{"   
partial_key = bytes([c ^ p for c, p in zip(cipher, known)])
print("Partial key (from prefix):", partial_key)
# Output: Partial key: myXORke'


key = b'myXORkey'  

full_key = (key * (len(cipher) // len(key) + 1))[:len(cipher)]
plaintext = bytes([c ^ k for c, k in zip(cipher, full_key)])
print(plaintext.decode())   
# Output: crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}