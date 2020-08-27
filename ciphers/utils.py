def int_to_bin(number: int, block_size=8) -> str:
    binary = bin(number)[2:]
    return '0' * (block_size - len(binary)) + binary


def char_2_num(letter: str) -> int:
    return ord(letter) - ord('a')


def num_2_char(number: int) -> str:
    return chr(ord('a') + number)


def mod(a, b):
    return a % b


def left_circ_shift(binary: str, shift: int) -> str:
    shift = shift % len(binary)
    return binary[shift:] + binary[0: shift]
