from mathematics import Polynomial


def int_to_bin(number: int, block_size=8) -> str:
    binary = bin(number)[2:]
    return '0' * (block_size - len(binary)) + binary


def char_2_num(letter: str) -> int:
    return ord(letter) - ord('a')


class Round:
    def __init__(self, key: int, func, block_size=8):
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


def polynomial_mod(p1: int, p2: int) -> int:
    return p1 % p2


round_cipher = Round(key=15, func=polynomial_mod, block_size=32)
letter = 'z'
plaintext_number = char_2_num(letter)
print('plaintext number:', plaintext_number)

ciphertext_number = round_cipher.encrypt(plaintext_number)
print('ciphertext number:', ciphertext_number)

decrypted = round_cipher.decrypt(ciphertext_number)
print('decrypted:', decrypted)

print(plaintext_number, ciphertext_number, decrypted)
