from mathematics import PBox
import numpy as np


class PermutationCipher:
    def __init__(self, key: list):
        self.pbox = PBox.from_list(key)
        self.inverse = self.pbox.invert()
        self.columns = len(key)

    def encrypt(self, plaintext: str) -> str:
        P = self.str_2_mat(plaintext)
        print(P)
        ciphertext = ''
        for index, row in enumerate(P):
            ciphertext += self.pbox.permutate(''.join(row)).upper()
        return ciphertext

    def decrypt(self, ciphertext: str) -> str:
        C = self.str_2_mat(ciphertext)
        plaintext = ''
        for index, row in enumerate(C):
            plaintext += self.inverse.permutate(''.join(row)).lower()
        return plaintext

    def str_2_mat(self, message: str):
        message = message + 'z' * (-len(message) % self.columns)
        rows = len(message) // self.columns
        return np.reshape(list(message), (rows, self.columns))
