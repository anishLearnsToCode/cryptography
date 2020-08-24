import numpy as np
from math import ceil


class ColumnTranspositionCipher:
    def __init__(self, rows):
        self.rows = rows

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ''
        for i in range(self.rows):
            for j in range(i, len(plaintext), self.rows):
                ciphertext += plaintext[j]
        return ciphertext.upper()

    def decrypt(self, ciphertext: str) -> str:
        columns = ceil(len(ciphertext) / self.rows)
        padding = len(ciphertext) % self.rows
        ciphertext += 'z' * padding
        C = np.reshape(list(ciphertext), (self.rows, columns))
        return ''.join(C.T.ravel())[: len(ciphertext) - padding].lower()
