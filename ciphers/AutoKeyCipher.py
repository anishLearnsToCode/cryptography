class AutoKeyCipher:
    def __init__(self, k):
        self.k = k

    def encrypt(self, plaintext):
        key = self.k
        ciphertext = ''
        for letter in plaintext.lower():
            ciphertext += chr((ord(letter) - ord('a') + key) % 26 + ord('A'))
            key = ord(letter) - ord('a')
        return ciphertext

    def decrypt(self, ciphertext):
        key = self.k
        plaintext = ''
        for letter in ciphertext.lower():
            key = (ord(letter) - ord('a') - key) % 26
            plaintext += chr(key + ord('a'))
        return plaintext
