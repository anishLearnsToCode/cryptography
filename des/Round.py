from des import NoneSwapper, Swapper, Mixer


class Round:
    def __init__(self, mixer):
        self.mixer = mixer
        self.swapper = NoneSwapper()

    @staticmethod
    def with_swapper(mixer: Mixer):
        temp = Round(mixer)
        temp.swapper = Swapper(block_size=mixer.block_size)
        return temp

    @staticmethod
    def without_swapper(mixer: Mixer):
        return Round(mixer)

    def encrypt(self, binary: str) -> str:
        binary = self.mixer.encrypt(binary)
        return self.swapper.encrypt(binary)

    def decrypt(self, binary: str) -> str:
        binary = self.swapper.decrypt(binary)
        return self.mixer.decrypt(binary)
