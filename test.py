from ciphers import CaesarShiftCipher

caesar_cipher = CaesarShiftCipher(10)
ciphertext = caesar_cipher.encrypt('helloworld')
print(ciphertext)
print(caesar_cipher.decrypt(ciphertext))
