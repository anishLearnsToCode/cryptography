from mathematics import multiplicative_inverse

class AffineCipher:
    def __init__(self, k_1, k_2):
        self.k_1 = k_1
        self.k_2 = k_2

    def char_to_num(self, letter):
        letter = letter.lower()
        return ord(letter) - ord('a')

    def encrypt(self, plaintext):
        return ''.join(
            [chr((self.char_to_num(letter) * self.k_1 + self.k_2) % 26 + ord('A')) for letter in plaintext.lower()])

    def decrypt(self, ciphertext):
        return ''.join(
            [chr(((self.char_to_num(letter) - self.k_2) * multiplicative_inverse(self.k_1, 26)) % 26 + ord('a'))
             for letter in ciphertext.lower()]
        )
