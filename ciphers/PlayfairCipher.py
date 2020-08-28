class PlayFairCipher:
    def __init__(self, key):
        self.key = key
        self.letter2index = self.get_letter_2_index_map()

    def get_letter_2_index_map(self):
        index_map = {}
        for row in range(len(self.key)):
            for column in range(len(self.key[row])):
                letter = self.key[row][column].lower()
                if letter == 'i':
                    index_map['j'] = (row, column)
                index_map[letter] = (row, column)
        return index_map

    def encrypt(self, plaintext):
        plaintext = self.pad_extra(self.remove_consecutive_same_chars(plaintext.lower()))
        # print('plaintext:', plaintext)
        ciphertext = ''
        for index in range(0, len(plaintext), 2):
            pair = plaintext[index: index + 2]
            ciphertext += self.encipher(pair)
        return ciphertext.upper()

    def decrypt(self, ciphertext):
        plaintext = ''
        for index in range(0, len(ciphertext), 2):
            pair = ciphertext[index: index + 2].lower()
            plaintext += self.decipher(pair)
        return plaintext

    def decipher(self, pair):
        row1, column1 = self.letter2index[pair[0]]
        row2, column2 = self.letter2index[pair[1]]
        if row1 == row2:
            return self.key[row1][(column1 - 1) % 5] + self.key[row1][(column2 - 1) % 5]
        elif column1 == column2:
            return self.key[(row1 - 1) % 5][column1] + self.key[(row2 - 1) % 5][column2]
        return self.key[row1][column2] + self.key[row2][column1]

    def encipher(self, pair):
        row1, column1 = self.letter2index[pair[0]]
        row2, column2 = self.letter2index[pair[1]]
        if row1 == row2:
            return self.key[row1][(column1 + 1) % 5] + self.key[row1][(column2 + 1) % 5]
        elif column1 == column2:
            return self.key[(row1 + 1) % 5][column1] + self.key[(row2 + 1) % 5][column2]
        return self.key[row1][column2] + self.key[row2][column1]

    @staticmethod
    def pad_extra(plaintext):
        return plaintext + PlayFairCipher.middle_character(plaintext[len(plaintext) - 1]) \
            if len(plaintext) % 2 == 1 else plaintext

    @staticmethod
    def remove_consecutive_same_chars(plaintext):
        for index in range(len(plaintext) - 1):
            if plaintext[index] == plaintext[index + 1]:
                plaintext = plaintext[: index + 1] + PlayFairCipher.middle_character(plaintext[index]) + plaintext[index + 1:]
        return plaintext

    @staticmethod
    def middle_character(letter):
        # return chr((ord(letter) - ord('a') + 1) % 26 + ord('a'))
        return 'x'
