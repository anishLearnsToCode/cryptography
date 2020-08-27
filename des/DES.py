from mathematics import PBox
from ciphers.utils import *
from des import *


class DES:
    def __init__(self, key: int):
        self.key = int_to_bin(key, block_size=64)
        self.PC_1 = PBox.des_key_initial_permutation()
        self.PC_2 = PBox.des_shifted_key_permutation()
        self.single_shift = {1, 2, 9, 16}
        self.rounds = self.generate_rounds()

    def encrypt(self, binary: str) -> str:
        for round in self.rounds:
            binary = round.encrypt(binary)
        return binary

    def decrypt(self, binary: str) -> str:
        for round in self.rounds[::-1]:
            binary = round.decrypt(binary)
        return binary

    def generate_rounds(self) -> list:
        rounds = []
        self.key = self.PC_1.permutate(self.key)
        l, r = self.key[0: 32], self.key[32:]
        for i in range(1, 17):
            shift = 1 if i in self.single_shift else 2
            l, r = left_circ_shift(l, shift), left_circ_shift(r, shift)
            key = int(self.PC_2.permutate(l + r), base=2)
            mixer = Mixer.des_mixer(key)
            cipher = Round.with_swapper(mixer) if i != 16 else Round.without_swapper(mixer)
            rounds.append(cipher)
        return rounds
