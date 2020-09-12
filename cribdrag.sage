'''
A general purpose Hill Cipher cracker using crib dragging of a known
plaintext. Supports 3x3 key matrices.
'''
import sys

KPT = "letusmeetxx"
# Proof of Concept
ciphertext = "HBCDFNOPIKLB"

trans_letter_to_num = {
        'A' : 0,
        'B' : 1,
        'C' : 2,
        'D' : 3,
        'E' : 4,
        'F' : 5,
        'G' : 6,
        'H' : 7,
        'I' : 8,
        'J' : 9,
        'K' : 10,
        'L' : 11,
        'M' : 12,
        'N' : 13,
        'O' : 14,
        'P' : 15,
        'Q' : 16,
        'R' : 17,
        'S' : 18,
        'T' : 19,
        'U' : 20,
        'V' : 21,
        'W' : 22,
        'X' : 23,
        'Y' : 24,
        'Z' : 25,
            }

trans_num_to_letter = {v: k for k, v in trans_letter_to_num.items()}

modulo = len(trans_num_to_letter)
print("Modulo: " + str(modulo))

print("Cipher Alphabet: ")
print(trans_num_to_letter)

def letter_to_num(c):
    return trans_letter_to_num[c]

def num_to_letter(n):
    return trans_num_to_letter[n]

def generate_keys(system1_solution, system2_solution, system3_solution):
    keys = []
    for (a, b, c) in system1_solution:
        for (d, e, f) in system2_solution:
            for (g, h, i) in system3_solution:
                keys.append([[a, b, c], [d, e, f], [g, h, i]])
    return keys

def text_mat_to_str(m):
    text = ""
    for c in range(len(m[0])):
        for r in range(len(m)):
            text += num_to_letter(int(m[r][c]))
    return text

def decrypt(trans_letter_to_num, ciphertext, KPT):
    if len(KPT) < 11:
        raise Exception("Known plaintext is too short. If you don't have enough "
                        "characters to meet the required length, please input a guess.")

    ciphertext = list(ciphertext)
    ciphertext = [letter_to_num(x) for x in ciphertext]

    ciphertext_blocks = []
    for x in range(0, len(ciphertext) - 2, 3):
        ciphertext_blocks.append([ciphertext[x], ciphertext[x+1], ciphertext[x+2]])
    print("Ciphertext: ",  ciphertext_blocks)

    ciphertext_blocks_mat = Matrix(IntegerModRing(modulo), ciphertext_blocks).transpose()

    #                   |a  b  c|
    # Solve for the key |d  e  f| such that (key * known plaintext = known ciphertext)
    #                   |g  h  i|
    # After the key is found, attempt to invert it. The original encryption key
    # must have been invertible. If the key is invertible, then invert it, and
    # right-multiply it by the ciphertext to get the decrypted plaintext.
    #   (key inverse * known ciphertext)
    # = (key inverse * key * known plaintext)
    # = (identity * known plaintext)
    # = known plaintext
    for offset in range(len(ciphertext)-len(KPT)+1):
        mapping = []
        if offset % 3 == 0:
            mapping.append((letter_to_num(KPT[0]), ciphertext[offset]))
            mapping.append((letter_to_num(KPT[1]), ciphertext[offset+1]))
            mapping.append((letter_to_num(KPT[2]), ciphertext[offset+2]))
            mapping.append((letter_to_num(KPT[3]), ciphertext[offset+3]))
            mapping.append((letter_to_num(KPT[4]), ciphertext[offset+4]))
            mapping.append((letter_to_num(KPT[5]), ciphertext[offset+5]))
            mapping.append((letter_to_num(KPT[6]), ciphertext[offset+6]))
            mapping.append((letter_to_num(KPT[7]), ciphertext[offset+7]))
            mapping.append((letter_to_num(KPT[8]), ciphertext[offset+8]))
        elif offset % 3 == 2:
            mapping.append((letter_to_num(KPT[1]), ciphertext[offset+1]))
            mapping.append((letter_to_num(KPT[2]), ciphertext[offset+2]))
            mapping.append((letter_to_num(KPT[3]), ciphertext[offset+3]))
            mapping.append((letter_to_num(KPT[4]), ciphertext[offset+4]))
            mapping.append((letter_to_num(KPT[5]), ciphertext[offset+5]))
            mapping.append((letter_to_num(KPT[6]), ciphertext[offset+6]))
            mapping.append((letter_to_num(KPT[7]), ciphertext[offset+7]))
            mapping.append((letter_to_num(KPT[8]), ciphertext[offset+8]))
            mapping.append((letter_to_num(KPT[9]), ciphertext[offset+9]))
        else:
            mapping.append((letter_to_num(KPT[2]), ciphertext[offset+2]))
            mapping.append((letter_to_num(KPT[3]), ciphertext[offset+3]))
            mapping.append((letter_to_num(KPT[4]), ciphertext[offset+4]))
            mapping.append((letter_to_num(KPT[5]), ciphertext[offset+5]))
            mapping.append((letter_to_num(KPT[6]), ciphertext[offset+6]))
            mapping.append((letter_to_num(KPT[7]), ciphertext[offset+7]))
            mapping.append((letter_to_num(KPT[8]), ciphertext[offset+8]))
            mapping.append((letter_to_num(KPT[9]), ciphertext[offset+9]))
            mapping.append((letter_to_num(KPT[10]), ciphertext[offset+10]))

        var('a', 'b', 'c')
        system1_solution = solve_mod([
                mapping[0][0]*a + mapping[1][0]*b + mapping[2][0]*c == mapping[0][1],
                mapping[3][0]*a + mapping[4][0]*b + mapping[5][0]*c == mapping[3][1],
                mapping[6][0]*a + mapping[7][0]*b + mapping[8][0]*c == mapping[6][1],
                ], modulo)
        if len(system1_solution) == 0:
            continue
        var('d', 'e', 'f')
        system2_solution = solve_mod([
                mapping[0][0]*d + mapping[1][0]*e + mapping[2][0]*f == mapping[1][1],
                mapping[3][0]*d + mapping[4][0]*e + mapping[5][0]*f == mapping[4][1],
                mapping[6][0]*d + mapping[7][0]*e + mapping[8][0]*f == mapping[7][1],
                ], modulo)
        if len(system2_solution) == 0:
            continue
        var('g', 'h', 'i')
        system3_solution = solve_mod([
                mapping[0][0]*g + mapping[1][0]*h + mapping[2][0]*i == mapping[2][1],
                mapping[3][0]*g + mapping[4][0]*h + mapping[5][0]*i == mapping[5][1],
                mapping[6][0]*g + mapping[7][0]*h + mapping[8][0]*i == mapping[8][1],
                ], modulo)
        if len(system3_solution) == 0:
            continue
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        #print "Possible solutions: "
        #print "(a, b, c): " + str(system1_solution)
        #print "(d, e, f): " + str(system2_solution)
        #print "(g, h, i): " + str(system3_solution)
        print("Offset: " + str(offset))
        for key in generate_keys(system1_solution, system2_solution, system3_solution):
            key_mat = Matrix(IntegerModRing(modulo), key)
            if key_mat.is_invertible():
                inv_key = key_mat.inverse()
                #print "Key: "
                #print key_mat.numpy()
                #print "Key inverse: "
                #print inv_key.numpy()
                print(text_mat_to_str((inv_key * ciphertext_blocks_mat).numpy()))
            else:
                #print "Key not invertible!"
                pass

if __name__ == '__main__':
    decrypt(trans_letter_to_num, ciphertext, KPT)