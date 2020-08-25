class KeyedTranspositionCipher:
    def __init__(self, key):
        self.key = key
        self.decryption_permutation = self.get_decryption_permutation()

    def encrypt(self, plaintext: str) -> str:
        padding = (- (len(plaintext) % len(self.key))) % len(self.key)
        plaintext = plaintext.lower() + 'z' * padding
        ciphertext = ''
        for index in range(0, len(plaintext), len(self.key)):
            block = plaintext[index: index + len(self.key)]
            ciphertext += self.encipher(block)
        return ciphertext.upper()

    def decrypt(self, ciphertext: str) -> str:
        plaintext = ''
        for index in range(0, len(ciphertext), len(self.key)):
            block = ciphertext[index: index + len(self.key)].lower()
            plaintext += self.decipher(block)
        return plaintext

    def decipher(self, block: str) -> str:
        return self.crypt(block, key=self.decryption_permutation)

    def encipher(self, block: str) -> str:
        return self.crypt(block, key=self.key)

    def crypt(self, block: str, key):
        encrypted = ['a'] * len(self.key)
        for index, letter in enumerate(block):
            encrypted[key[index]] = letter
        return ''.join(encrypted)

    def get_decryption_permutation(self):
        permutation = [0] * len(self.key)
        for index, value in enumerate(self.key):
            permutation[value] = index
        return permutation
