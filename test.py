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

# mixer = Mixer.des_mixer(key=3)
number = 1234
binary = int_to_bin(number, block_size=64)

# round1 = Round.without_swapper(mixer)
# ciphertext = round1.encrypt(binary)
# print(ciphertext)
# print(int(round1.decrypt(ciphertext), base=2))

# multiple rounds
# rounds = [Round.with_swapper(Mixer.des_mixer(key=3)),
#           Round.with_swapper(Mixer.des_mixer(key=5)),
#           Round.without_swapper(Mixer.des_mixer(key=7))
#           ]

# for r in rounds:
#     binary = r.encrypt(binary)
# print(binary)

# for r in rounds[::-1]:
#     binary = r.decrypt(binary)
# print(binary)
# print(int(binary, base=2))

des = DES(key=78)
ciphertext = des.encrypt(binary)
print(ciphertext)

print(int(des.decrypt(ciphertext), base=2))

# pbox = PBox.des_single_round_expansion()
# print(pbox.permutate(int_to_bin(1234, block_size=32)))
