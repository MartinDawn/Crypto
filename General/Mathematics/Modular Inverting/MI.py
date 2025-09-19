def egcd(a, b):
    """Extended gcd. Returns (g, x, y) with a*x + b*y = g."""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    return x % m


print(modinv(3, 13))  # Output 9
