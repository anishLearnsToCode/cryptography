class Swapper:
    def __init__(self, block_size=64):
        self.block_size = block_size

    def encrypt(self, binary: str) -> str:
        l, r = binary[0: self.block_size // 2], binary[self.block_size // 2:]
        return r + l

    def decrypt(self, binary: str) -> str:
        return self.encrypt(binary)
