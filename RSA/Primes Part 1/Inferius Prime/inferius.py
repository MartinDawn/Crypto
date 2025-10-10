

from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

e = 65537

p = 848445505077945374527983649411#fROM FACTORDB.COM
q = 1160939713152385063689030212503
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

n = 984994081290620368062168960884976209711107645166770780785733

FLAG = b"crypto{???????????????}"
pt = bytes_to_long(FLAG)
# ct = pow(pt, e, n)
ct = 948553474947320504624302879933619818331484350431616834086273

print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")

pt = pow(ct, d, n)
decrypted = long_to_bytes(pt)
print(pt, decrypted)
