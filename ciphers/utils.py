import numpy as np


def int_to_bin(number: int, block_size=8) -> str:
    binary = bin(number)[2:]
    return '0' * (block_size - len(binary)) + binary


def char_2_num(letter: str) -> int:
    return ord(letter.lower()) - ord('a')


def token_2_num(word: str) -> list:
    return [char_2_num(letter) for letter in word]


def to_val(word: str, base: int = 26) -> int:
    value = 0
    for index, letter in enumerate(word[::-1]):
        value += char_2_num(letter) * pow(base, index)
    return value


def incidence_of_coincidence(frequency: list) -> float:
    f = np.array(frequency)
    N = f.sum()
    return (f * (f - 1)).sum() / (N * (N - 1))


def num_2_char(number: int) -> str:
    return chr(ord('a') + number)


def mod(a, b):
    return a % b


def left_circ_shift(binary: str, shift: int) -> str:
    shift = shift % len(binary)
    return binary[shift:] + binary[0: shift]
