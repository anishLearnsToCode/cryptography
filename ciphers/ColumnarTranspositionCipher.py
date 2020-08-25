import numpy as np


class ColumnarTranspositionCipher:
    def __init__(self, key: list):
        self.key = key
        self.key_inv = self.inv(key)

    def encrypt(self, plaintext: str) -> str:
        A = self.str_2_mat(plaintext)
        A = A[:, self.key]
        return self.mat_2_str(A.T).upper()

    def decrypt(self, ciphertext: str) -> str:
        C = self.str_2_mat_column_wise(ciphertext)
        C = C[:, self.key_inv]
        return self.mat_2_str(C).lower()

    def str_2_mat_column_wise(self, text: str):
        rows, columns = len(self.key), len(text) // len(self.key)
        return np.reshape(list(text), (rows, columns)).T

    def str_2_mat(self, text: str):
        padding = (- (len(text) % len(self.key))) % len(self.key)
        text = text + 'z' * padding
        rows, columns = len(text) // len(self.key), len(self.key)
        return np.reshape(list(text), (rows, columns))

    @staticmethod
    def inv(key: list) -> list:
        inv_key = [0] * len(key)
        for index, value in enumerate(key):
            inv_key[value] = index
        return inv_key

    @staticmethod
    def mat_2_str(matrix) -> str:
        return ''.join(matrix.ravel())
