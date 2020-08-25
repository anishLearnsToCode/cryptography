class Permutation(object):
    def __init__(self, permutation: list):
        self.permutation = permutation
        self.permutation_map = self.get_permutations_map(permutation)

    def value(self, index: int) -> int:
        return self.permutation[index]

    def permutate(self, sequence: list) -> list:
        result = [0] * len(sequence)
        for index, value in enumerate(sequence):
            result[self.permutation_map[index] - 1] = value
        return result

    def get_permutations_map(self, permutation: list) -> list:
        result = [0] * len(permutation)
        for index, value in enumerate(permutation):
            result[value - 1] = index + 1
        return result

    def compose(self, p):
        permutations = [0] * len(self.permutation)
        for index, value in enumerate(self.permutation):
            permutations[index] = p.permutation[value - 1]
        return Permutation(permutations)


# composition of permutations
p1 = Permutation([3, 1, 2])
p2 = Permutation([1, 3, 2])
print(p2.permutate([10, 20, 30]))
p3 = p2.compose(p1)
print(p3.permutation)
