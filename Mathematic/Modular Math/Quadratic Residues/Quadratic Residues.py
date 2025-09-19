p=29; ints=[14,6,11]
for x in ints:
    sols=[a for a in range(1,p) if a*a%p==x]
    print(x, "->", sols or "non-residue")
# shows 6 -> [8,21]
