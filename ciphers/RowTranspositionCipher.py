from ciphers import ColumnTranspositionCipher


class RowTranspositionCipher:
    def __init__(self, columns):
        self.cipher = ColumnTranspositionCipher(rows=columns)

    def encrypt(self, plaintext: str) -> str:
        return self.cipher.encrypt(plaintext)

    def decrypt(self, ciphertext: str) -> str:
        return self.cipher.decrypt(ciphertext)
