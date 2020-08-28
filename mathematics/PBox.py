class PBox:
    def __init__(self, key: dict):
        self.key = key
        self.in_degree = len(key)
        self.out_degree = sum(len(value) if isinstance(value, list) else 1 for value in key.values())

    def __repr__(self) -> str:
        return 'PBox' + str(self.key)

    def permutate(self, sequence: list) -> str:
        result = [0] * self.out_degree
        for index, value in enumerate(sequence):
            if (index + 1) in self.key:
                indices = self.key.get(index + 1, [])
                indices = indices if isinstance(indices, list) else [indices]
                for i in indices:
                    result[i - 1] = value
        return ''.join(map(str, result))

    def is_invertible(self) -> bool:
        return self.in_degree == self.out_degree

    def invert(self):
        if self.is_invertible():
            result = {}
            for index, mapping in self.key.items():
                result[mapping[0]] = index
            return PBox(result)

    @staticmethod
    def identity(block_size=64):
        return PBox({index: index for index in range(1, block_size + 1)})

    @staticmethod
    def from_list(permutation: list):
        mapping = {}
        for index, value in enumerate(permutation):
            indices = mapping.get(value, [])
            indices.append(index + 1)
            mapping[value] = indices
        return PBox(mapping)

    @staticmethod
    def des_initial_permutation():
        return PBox.from_list(
            [58, 50, 42, 34, 26, 18, 10, 2,
             60, 52, 44, 36, 28, 20, 12, 4,
             62, 54, 46, 38, 30, 22, 14, 6,
             64, 56, 48, 40, 32, 24, 16, 8,
             57, 49, 41, 33, 25, 17, 9, 1,
             59, 51, 43, 35, 27, 19, 11, 3,
             61, 53, 45, 37, 29, 21, 13, 5,
             63, 55, 47, 39, 31, 23, 15, 7]
        )

    @staticmethod
    def des_final_permutation():
        return PBox.from_list(
            [40, 8, 48, 16, 56, 24, 64, 32,
             39, 7, 47, 15, 55, 23, 63, 31,
             38, 6, 46, 14, 54, 22, 62, 30,
             37, 5, 45, 13, 53, 21, 61, 29,
             36, 4, 44, 12, 52, 20, 60, 28,
             35, 3, 43, 11, 51, 19, 59, 27,
             34, 2, 42, 10, 50, 18, 58, 26,
             33, 1, 41, 9, 49, 17, 57, 25]
        )

    @staticmethod
    def des_single_round_expansion():
        """This is the Permutation made on the right half of the block to convert 32 bit --> 42 bits in DES Mixer"""
        return PBox.from_list(
            [32, 1, 2, 3, 4, 5,
             4, 5, 6, 7, 8, 9,
             8, 9, 10, 11, 12, 13,
             12, 13, 14, 15, 16, 17,
             16, 17, 18, 19, 20, 21,
             20, 21, 22, 23, 24, 25,
             24, 25, 26, 27, 28, 29,
             28, 29, 30, 31, 32, 1]
        )

    @staticmethod
    def des_single_round_final():
        """This is the permutation made after the substitution happens in each round"""
        return PBox.from_list(
            [16, 7, 20, 21, 29, 12, 28, 17,
             1, 15, 23, 26, 5, 18, 31, 10,
             2, 8, 24, 14, 32, 27, 3, 9,
             19, 13, 30, 6, 22, 11, 4, 25]
        )

    @staticmethod
    def des_key_initial_permutation():
        return PBox.from_list(
            [57, 49, 41, 33, 25, 17, 9,
             1, 58, 50, 42, 34, 26, 18,
             10, 2, 59, 51, 43, 35, 27,
             19, 11, 3, 60, 52, 44, 36,
             63, 55, 47, 39, 31, 23, 15,
             7, 62, 54, 46, 38, 30, 22,
             14, 6, 61, 53, 45, 37, 29,
             21, 13, 5, 28, 20, 12, 4]
        )

    @staticmethod
    def des_shifted_key_permutation():
        """PC2 Matrix for compression PBox 56 bit --> 48 bit"""
        return PBox.from_list(
            [14, 17, 11, 24, 1, 5, 3, 28,
             15, 6, 21, 10, 23, 19, 12, 4,
             26, 8, 16, 7, 27, 20, 13, 2,
             41, 52, 31, 37, 47, 55, 30, 40,
             51, 45, 33, 48, 44, 49, 39, 56,
             34, 53, 46, 42, 50, 36, 29, 32]
        )
