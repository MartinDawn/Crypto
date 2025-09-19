# Đọc ciphertext từ file
with open("output.txt", "r") as f:
    content = f.read()
    cipher = eval(content)  # chuyển chuỗi trong file thành list Python

p = 1007621497415251  # prime đã cho

bits = []
for n in cipher:
    leg = pow(n, (p-1)//2, p)  # tính Legendre symbol
    if leg == 1:
        bits.append('1')
    else:
        bits.append('0')  # nếu leg == p-1

# Gom 8 bit thành 1 byte
flag_bytes = []
for i in range(0, len(bits), 8):
    byte = bits[i:i+8]
    flag_bytes.append(int(''.join(byte), 2))

flag = bytes(flag_bytes)
print(flag.decode())
# crypto{p4tterns_1n_re5idu3s}
