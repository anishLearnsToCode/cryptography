from ciphers.utils import *
from mathematics import PBox
from mathematics import SBox
from des import *

number = 12345
binary = int_to_bin(number, block_size=64)
des = DES(key=78)
# ciphertext = des.encrypt(binary)
# print(ciphertext)
#
# print(int(des.decrypt(ciphertext), base=2))

message = 'hello world 😀'
ciphertext = des.encrypt_message(message)
print(ciphertext)
print(des.decrypt_message(ciphertext))
