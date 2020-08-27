from ciphers.utils import *
from mathematics import PBox
from mathematics import SBox
from des import *


# swapper = Swapper()
# ciphertext = swapper.encrypt(123456)
# print(ciphertext)
# print(swapper.decrypt(ciphertext))
#
# s_box = SBox(block_size=2, table={
#     (0, 0): 0,
#     (0, 1): 1,
#     (1, 0): 2,
#     (1, 1): 3
# }, func=lambda x: (x[0], x[1]))

# print(s_box('00'))
# print(s_box('01'))
# print(s_box('10'))
# print(s_box('11'))

# s_box = SBox.des_s_box_1()

# binary = '000100'
# print(s_box(binary))
# print(s_box2(binary))

# p_box = PBox.des_initial_permutation()
# print(p_box.permutate(int_to_bin(1, block_size=64)))
#
# mixer = Mixer(key=10)


# ciphertext = mixer.encrypt(int_to_bin(1234, block_size=64))
# print(ciphertext)

# round_cipher = Round.with_swapper(mixer)
# round_cipher_wihout = Round.without_swapper(mixer)
# print(round_cipher.encrypt(int_to_bin(1234, block_size=64)))
# print(round_cipher_wihout.encrypt(int_to_bin(1234, block_size=64)))

mixer = Mixer(key=3,
              initial_permutation=PBox.des_single_round_expansion(),
              final_permutation=PBox.des_single_round_final(),
              func=lambda a, b: a ^ b)

ciphertext = mixer.encrypt(int_to_bin(1234, block_size=64))
print(ciphertext)
print(int(mixer.encrypt(ciphertext), base=2))


# pbox = PBox.des_single_round_expansion()
# print(pbox.permutate(int_to_bin(1234, block_size=32)))

