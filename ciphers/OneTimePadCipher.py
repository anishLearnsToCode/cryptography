from ciphers import VignereCipher
import numpy as np


class OneTimePadCipher:
    def __init__(self):
        self.key = ''
        self.pad_used = False
        self.cipher = None

    def encrypt(self, plaintext: str):
        if not self.pad_used:
            self.pad_used = True
            self.generate_random_key(plaintext)
            self.cipher = VignereCipher(self.key)
            return self.cipher.encrypt(plaintext)
        else:
            return None

    def decrypt(self, ciphertext: str):
        if not self.pad_used:
            return None
        else:
            return self.cipher.decrypt(ciphertext)

    def generate_random_key(self, plaintext: str) -> None:
        self.key = ''.join(list(map(self.num_2_char, np.random.randint(0, 25, len(plaintext)))))

    @staticmethod
    def num_2_char(number: int) -> str:
        return chr(number + ord('a'))
