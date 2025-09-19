from Crypto.Util.number import long_to_bytes

n = 11515195063862318899931685488813747395775516287289682636499965282714637259206269


decoded_bytes = long_to_bytes(n)


message = decoded_bytes.decode("utf-8")

print(message)
# Output: crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}
