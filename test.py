from mathematics import gcd, extended_gcd, diophantine, diophantine_general

# print(gcd(25, 60))
# hcf, s, t = extended_gcd(161, 28)
# print(s * 161 + t * 28, hcf)
#
# hcf, s, t = extended_gcd(10, 2)
# print(s * 10 + t * 2, hcf)
#
# hcf, s, t = extended_gcd(0, 45)
# print(s * 0 + t * 45, hcf)

print(diophantine(21, 14, 35))

for x, y in diophantine_general(20, 5, 100):
    print(x, y)
