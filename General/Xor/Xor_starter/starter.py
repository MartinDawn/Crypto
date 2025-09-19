from pwn import xor

if __name__ == "__main__":
    label = "label"  

    # xor từng kí tự với 13 và in ra kết quả
    print("crypto{" + ''.join(chr(ord(c) ^ 13) for c in label) + "}")
    # output: crypto{aloha}
