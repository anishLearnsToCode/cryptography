from ciphers import ColumnTranspositionCipher

cipher = ColumnTranspositionCipher(2)
ciphertext = cipher.encrypt('meetmeatthepark')
print(ciphertext)

print(cipher.decrypt(ciphertext))
