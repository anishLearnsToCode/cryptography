from mathematics import *
from ciphers import *
import numpy as np

plaintext = 'meetmelater'

caesar_cipher = CaesarShiftCipher(shift=23)
permutation_cipher = PermutationCipher(key=[3, 5, 2, 4, 1])

ciphertext = caesar_cipher.encrypt(plaintext)

print(ciphertext)
print(permutation_cipher.encrypt(ciphertext))