from ciphers import ColumnTranspositionCipher


class RailFenceCipher:
    def __init__(self):
        self.cipher = ColumnTranspositionCipher(rows=2)

    def encrypt(self, plaintext: str) -> str:
        return self.cipher.encrypt(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self.cipher.decrypt(ciphertext)
