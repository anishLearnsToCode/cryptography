from mathematics import *
import random


p, q = 7, 11
n = p * q
print('n:', n)
phi_n = totient(n)
print('totient:', phi_n)
phi_n_list = relatively_prime_numbers(phi_n)
print('relatively prime numbers to phi(n):', phi_n_list)
# e = phi_n_list[random.randint(0, len(phi_n_list))]
e = 13
print('e:', e)
d = multiplicative_inverse(e, phi_n)
print('d:', d)

# m = random.randint(0, n)
m = 8
# c = pow(m, e, n)
c = 20
print('plaintext:', m)
print('ciphertext:', c)

p = pow(c, d, n)
print('decrypted:', p)
