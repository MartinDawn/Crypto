def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(66528, 52920))  # 1512
print(gcd(26513, 32321))  