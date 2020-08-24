class VignereCipher:
    def __init__(self, key: str):
        self.key = key

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ''
        for index, letter in enumerate(plaintext.lower()):
            ciphertext += chr((self.char_2_num(letter) + self.char_2_num(self.key[index % len(self.key)])) % 26 + ord('a'))
        return ciphertext.upper()

    def decrypt(self, ciphertext: str) -> str:
        plaintext = ''
        for index, letter in enumerate(ciphertext.lower()):
            plaintext += chr(
                (self.char_2_num(letter) - self.char_2_num(self.key[index % len(self.key)])) % 26 + ord('a'))
        return plaintext.lower()

    @staticmethod
    def char_2_num(character: str) -> int:
        return ord(character.lower()) - ord('a')
