from mathematics import PBox
from ciphers.utils import *
from des import *


class DES:
    def __init__(self, key: int):
        self.key = int_to_bin(key, block_size=64)
        self.PC_1 = PBox.des_key_initial_permutation()
        self.PC_2 = PBox.des_shifted_key_permutation()
        self.P_i = PBox.des_initial_permutation()
        self.P_f = PBox.des_final_permutation()
        self.single_shift = {1, 2, 9, 16}
        self.rounds = self.generate_rounds()

    def encrypt(self, binary: str) -> str:
        binary = self.P_i.permutate(binary)
        for round in self.rounds:
            binary = round.encrypt(binary)
        return self.P_f.permutate(binary)

    def decrypt(self, binary: str) -> str:
        binary = self.P_f.invert().permutate(binary)
        for round in self.rounds[::-1]:
            binary = round.decrypt(binary)
        return self.P_i.invert().permutate(binary)

    def encrypt_message(self, plaintext: str) -> list:
        result = [0] * len(plaintext)
        for index, letter in enumerate(plaintext.lower()):
            result[index] = int(self.encrypt(int_to_bin(ord(letter), block_size=64)), base=2)
        return result

    def decrypt_message(self, ciphertext_stream: list) -> str:
        return ''.join(map(chr, self.plaintext_stream(ciphertext_stream)))

    def plaintext_stream(self, ciphertext_stream: list) -> list:
        return [int(self.decrypt(int_to_bin(number, block_size=64)), base=2) for number in ciphertext_stream]

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
