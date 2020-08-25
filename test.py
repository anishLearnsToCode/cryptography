from ciphers import ColumnarTranspositionCipher

key_transposition_cipher = ColumnarTranspositionCipher(key=[2, 0, 3, 4, 1])
ciphertext = key_transposition_cipher.encrypt('enemyattackstonight')
print(ciphertext)

print(key_transposition_cipher.decrypt(ciphertext))
