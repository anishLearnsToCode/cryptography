from mathematics import multiplicative_inverse


class MultiplicativeCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext: str) -> str:
        return ''.join([self.num_2_char((self.char_2_num(letter) * self.key) % 26) for letter in plaintext.lower()])

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(
            [self.num_2_char((self.char_2_num(letter) * multiplicative_inverse(self.key, 26)) % 26)
             for letter in ciphertext.lower()]
        )

    @staticmethod
    def char_2_num(character: str) -> int:
        return ord(character.lower()) - ord('a')

    @staticmethod
    def num_2_char(number: int) -> str:
        return chr(number + ord('a'))
