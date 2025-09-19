# extended_gcd.py
def egcd(a, b):
    """Extended Euclidean algorithm.
    Returns (g, x, y) such that a*x + b*y = g = gcd(a,b).
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

p = 26513
q = 32321
g, u, v = egcd(p, q)

print("u =", u)
print("v =", v)
output = -8404
