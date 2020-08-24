from ciphers import OneTimePadCipher

cipher = OneTimePadCipher()
ciphertext = cipher.encrypt('helloworld')
print(ciphertext)
print(cipher.decrypt(ciphertext))
print(cipher.encrypt('zombie'))
print(cipher.decrypt('lolz'))