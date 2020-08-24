class CaesarShiftCipher:
    def __init__(self, shift=1):
        self.shift = shift

    def encrypt(self, plaintext):
        return ''.join(
            [self.num_2_char((self.char_2_num(letter) + self.shift) % 26) for letter in plaintext.lower()]
        ).upper()

    def decrypt(self, ciphertext: str) -> str:
        return ''.join(
            [self.num_2_char((self.char_2_num(letter) - self.shift) % 26) for letter in ciphertext.lower()]
        ).lower()

    @staticmethod
    def char_2_num(character: str) -> int:
        return ord(character.lower()) - ord('a')

    @staticmethod
    def num_2_char(number: int) -> str:
        return chr(number + ord('a'))
