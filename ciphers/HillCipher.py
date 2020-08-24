import numpy as np
from mathematics import modMatInv


class HillCipher:
    def __init__(self, key):
        self.key = key
        self.block_size = len(key)
        self.key_inv = modMatInv(self.key, 26)

    def encrypt(self, plaintext: str) -> str:
        P = self.text_2_mat(plaintext)
        C = P.dot(self.key) % 26
        return self.mat_2_text(C).upper()

    def decrypt(self, ciphertext: str) -> str:
        C = self.text_2_mat(ciphertext)
        P = C.dot(self.key_inv) % 26
        return self.mat_2_text(P).lower()

    def text_2_mat(self, text: str):
        text = self.pad_chars(text.lower()).lower()
        l = len(text) // self.block_size
        return np.reshape(list(map(self.char_2_num, text)), (l, self.block_size))

    def mat_2_text(self, matrix) -> str:
        return ''.join(list(map(self.num_2_char, list(matrix.ravel()))))

    @staticmethod
    def char_2_num(character: str) -> int:
        character = character.lower()
        return ord(character) - ord('a')

    @staticmethod
    def num_2_char(number: int) -> str:
        return chr(int(number) + ord('A'))

    def pad_chars(self, plaintext: str) -> str:
        padding = (- (len(plaintext) % self.block_size)) % self.block_size
        return plaintext + 'z' * padding
