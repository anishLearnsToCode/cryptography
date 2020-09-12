from ciphers import ColumnTranspositionCipher


class RailFenceCipher:
    def __init__(self, rails=2):
        self.rails = rails
        self.rails_indices = [i for i in range(self.rails)] + [i for i in range(self.rails - 2, 0, -1)]
        print(self.rails_indices)

    def encrypt(self, plaintext: str) -> str:
        rows = [''] * self.rails
        for index, letter in enumerate(plaintext.lower()):
            rows[self.rails_indices[index % len(self.rails_indices)]] += letter
        return ''.join(rows).upper()
