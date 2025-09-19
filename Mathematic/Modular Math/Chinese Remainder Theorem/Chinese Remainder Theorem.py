def chinese_remainder_theorem(remainders, moduli):
    # N là tích các modulus
    N = 1
    for m in moduli:
        N *= m

    result = 0
    for (a_i, n_i) in zip(remainders, moduli):
        N_i = N // n_i
        # nghịch đảo của N_i mod n_i
        inv = pow(N_i, -1, n_i)
        result += a_i * N_i * inv

    return result % N


remainders = [2, 3, 5]   # x ≡ 2 mod 5, x ≡ 3 mod 11, x ≡ 5 mod 17
moduli = [5, 11, 17]

a = chinese_remainder_theorem(remainders, moduli)
print("a =", a)   #  872
