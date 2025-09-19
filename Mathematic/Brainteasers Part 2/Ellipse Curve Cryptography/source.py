# solve_by_mapping.py
# Yêu cầu: Python3, sympy (để factorint). Nếu không có sympy, cài: pip install sympy

from math import isqrt
from collections import defaultdict
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from hashlib import sha1
from Crypto.Util.number import inverse, long_to_bytes
import sympy as sp

# params (từ output.txt)
p = 173754216895752892448109692432341061254596347285717132408796456167143559
D = 529
G = (29394812077144852405795385333766317269085018265469771684226884125940148,
     94108086667844986046802106544375316173742538919949485639896613738390948)
A = (155781055760279718382374741001148850818103179141959728567110540865590463,
     73794785561346677848810778233901832813072697504335306937799336126503714)
B = (171226959585314864221294077932510094779925634276949970785138593200069419,
     54353971839516652938533335476115503436865545966356461292708042305317630)

iv_hex = '64bc75c8b38017e1397c46f85d4e332b'
c_hex  = '13e4d200708b786d8f7c3bd2dc5de0201f0d7879192e6603d7c5d6b963e1df2943e3ff75f7fda9c30a92171bbbc5acbf'

# helper: compute z = x + 23*y mod p
def phi(P):
    x,y = P
    return (x + 23 * y) % p

# BSGS in multiplicative group modulo p
def baby_step_giant_step(base, target, order_bound=None):
    """Return x such that base^x = target mod p, or None if not found.
       If order_bound is known (the subgroup order), pass it as order_bound."""
    if base % p == 0 or target % p == 0:
        return None
    if order_bound is None:
        N = p-1
    else:
        N = order_bound
    m = int(isqrt(N) + 1)
    baby = {}
    curr = 1
    for j in range(m):
        if curr not in baby:
            baby[curr] = j
        curr = (curr * base) % p
    # compute base^{-m}
    base_m = pow(base, m, p)
    inv_base_m = pow(base_m, -1, p)
    gamma = target
    for i in range(m):
        if gamma in baby:
            return i*m + baby[gamma]
        gamma = (gamma * inv_base_m) % p
    return None

# Pohlig-Hellman using factorization of p-1
def discrete_log_pohlig_hellman(base, target):
    N = p - 1
    fac = sp.factorint(N)   # requires sympy
    # store congruences x = x_i mod p_i^e_i
    residues = []
    for q, e in fac.items():
        pe = q**e
        # compute g_i = base^{(N/pe)}, h_i = target^{(N/pe)}
        exp = N // pe
        g_i = pow(base, exp, p)
        h_i = pow(target, exp, p)
        if g_i == 1:
            # then discrete log modulo pe is 0
            residues.append((0, pe))
            continue
        # find x modulo pe; use lifting by solving for each digit
        x_mod_pe = 0
        cur = 1
        # we will compute x = x0 + x1*q + x2*q^2 + ... up to q^e
        for k in range(e):
            # compute h_k = h * g^{-x_mod_pe} ^(q^k) ??? Standard way:
            exponent = N // (q**(k+1))
            gk = pow(base, exponent, p)
            hk = pow((target * pow(base, -x_mod_pe, p)) % p, exponent, p)
            # now solve gk^{alpha} = hk in group of order q
            # use BSGS in small group of order q
            alpha = baby_step_giant_step(gk, hk, order_bound=q)
            if alpha is None:
                # fallback: try brute force (q small)
                found = None
                for t in range(q):
                    if pow(gk, t, p) == hk:
                        found = t
                        break
                if found is None:
                    raise ValueError(f"Cannot solve discrete log for prime {q}")
                alpha = found
            x_mod_pe += alpha * (q**k)
        residues.append((x_mod_pe, pe))
    # CRT combine residues
    x = 0
    M = 1
    for _, pe in residues:
        M *= pe
    for r, pe in residues:
        Mi = M // pe
        invMi = pow(Mi, -1, pe)
        x = (x + r * Mi * invMi) % M
    return x, M

def main():
    base = phi(G)
    targA = phi(A)
    targB = phi(B)
    print("base (phi(G)) =", base)
    print("phi(A) =", targA)
    print("phi(B) =", targB)

    # compute discrete log n_a such that base^n_a = phi(A) mod p
    print("computing discrete log (this may take a moment, needs sympy)...")
    n_a, mod_order = discrete_log_pohlig_hellman(base, targA)
    print("n_a (mod order) =", n_a, "modulo", mod_order)
    # If mod_order < true exponent or if not fully solved, n_a is known modulo mod_order.
    # Now compute shared as targB^n_a
    sharedZ = pow(targB, n_a, p)
    # x-coordinate from z: x = (z + z^{-1})/2 mod p
    inv2 = pow(2, -1, p)
    sharedZ_inv = pow(sharedZ, -1, p)
    shared_x = ((sharedZ + sharedZ_inv) * inv2) % p
    print("shared x:", shared_x)

    # derive AES key and decrypt
    key = sha1(str(shared_x).encode('ascii')).digest()[:16]
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import unpad
    ct = bytes.fromhex(c_hex)
    iv = bytes.fromhex(iv_hex)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), 16)
    print("plaintext:", pt.decode())

if __name__ == "__main__":
    main()
