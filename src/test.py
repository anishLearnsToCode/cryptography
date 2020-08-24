from src.mathematics import diophantine, diophantine_general, PlayFairCipher

# print(gcd(25, 60))
# hcf, s, t = extended_gcd(161, 28)
# print(s * 161 + t * 28, hcf)
#
# hcf, s, t = extended_gcd(10, 2)
# print(s * 10 + t * 2, hcf)
#
# hcf, s, t = extended_gcd(0, 45)
# print(s * 0 + t * 45, hcf)

playfair_cipher = PlayFairCipher(
    [['l', 'g', 'd', 'b', 'a'],
     ['q', 'm', 'h', 'e', 'c'],
     ['u', 'r', 'n', 'i', 'f'],
     ['x', 'v', 's', 'o', 'k'],
     ['z', 'y', 'w', 't', 'p']]
)

ciphertext = playfair_cipher.encrypt('hello')
print(ciphertext)
