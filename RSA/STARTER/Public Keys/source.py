# C =  m^e mod N
# Tính hàm phi euler: phi(N) = (p-1)(q-1)
# Giả sử N = 391, e = 65537, m = 12
phiEuler = (17 - 1) * (23 - 1)  
e = 65537%phiEuler
value = pow(12, e, 17*23)
print(value)
# Output:  301