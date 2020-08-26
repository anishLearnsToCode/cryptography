class PBox:
    def __init__(self, key: dict):
        self.key = key
        self.in_degree = len(key)
        self.out_degree = sum(len(value) if isinstance(value, list) else 1 for value in key.values())

    def __repr__(self) -> str:
        return 'PBox' + str(self.key)

    def permutate(self, sequence: list) -> list:
        result = [0] * self.out_degree
        for index, value in enumerate(sequence):
            if (index + 1) in self.key:
                indices = self.key.get(index + 1, [])
                indices = indices if isinstance(indices, list) else [indices]
                for i in indices:
                    result[i - 1] = value
        return result

    def is_invertible(self) -> bool:
        return self.in_degree == self.out_degree

    def invert(self):
        if self.is_invertible():
            result = {}
            for index, mapping in self.key.items():
                result[mapping] = index
            return PBox(result)
