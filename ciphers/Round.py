from ciphers.utils import *


class Round:
    def __init__(self, key: int, func, block_size=32):
        # key = int_to_bin(key)
        self.key = key
        self.func = func
        self.block_size = block_size

    def encrypt(self, plaintext_number: int) -> int:
        l1, r1 = self.binary_fragments(plaintext_number, self.block_size // 2)
        f1 = self.func(r1, self.key)
        r2 = f1 ^ l1
        l2 = r1
        result = int_to_bin(l2, self.block_size // 2) + int_to_bin(r2, self.block_size // 2)
        return int(result, base=2)

    def decrypt(self, cipher_number: int) -> int:
        l2, r2 = self.binary_fragments(cipher_number, self.block_size // 2)
        f = self.func(r2, self.key)
        l1 = r2 ^ f
        r1 = l2
        result = int_to_bin(l1, self.block_size // 2) + int_to_bin(r1, self.block_size // 2)
        return int(result, base=2)

    @staticmethod
    def binary_fragments(number, block_size=4):
        binary = int_to_bin(number, 2 * block_size)
        l = binary[0: block_size]
        r = binary[block_size:]
        return int(l, base=2), int(r, base=2)
