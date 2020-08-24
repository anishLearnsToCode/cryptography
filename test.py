from mathematics import modMatInv
from ciphers.HillCipher import HillCipher

hill_cipher = HillCipher([
    [9, 7, 11, 13],
    [4, 7, 5, 6],
    [2, 21, 14, 9],
    [3, 23, 21, 8]
])

ciphertext = hill_cipher.encrypt('codeisready')
print(ciphertext)
print(hill_cipher.decrypt(ciphertext))

# print(modMatInv([
#     [9, 7, 11, 13],
#     [4, 7, 5, 6],
#     [2, 21, 14, 9],
#     [3, 23, 21, 8]
# ], 26))
