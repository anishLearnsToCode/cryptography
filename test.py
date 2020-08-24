from ciphers import MultiplicativeCipher

caesar_cipher = MultiplicativeCipher(7)
ciphertext = caesar_cipher.encrypt('helloworld')
print(ciphertext)
print(caesar_cipher.decrypt(ciphertext))
