from collections import Counter


def substitution(text: str, mapping: dict):
    result = ''
    for letter in text:
        if letter in mapping:
            result += mapping[letter]
        else:
            result += letter
    return result


def get_mapping(order: list, counter: Counter) -> dict:
    result = {}
    i = 0
    while len(counter) > 0:
        most_common = counter.most_common(1)[0][0]
        result[most_common] = order[i]
        i += 1
        del counter[most_common]
    return result


# noinspection SpellCheckingInspection
ciphertext = 'EMGLOSUDCGDNCUSWYSFHNSFCYKDPUMLWGYICOXYSIPJCKQPKUGKMGOLICGINCGACKSNISACYKZSCKXECJCKSHYSXCGOIDPKZCNKSHICGIWYGKKGKGOLDSILKGOIUSIGLEDSPWZUGFZCCNDGYYSFUSZCNXEOJNCGYEOWEUPXEZGACGNFGLKNSACIGOIYCKXCJUCIUZCFZCCNDGYYSFEUEKUZCSOCFZCCNCIACZEJNCSHFZEJZEGMXCYHCJUMGKUCY'

print(ciphertext, '\n')
monogram_freq = Counter(ciphertext)
bigram_freq = Counter(ciphertext[i: i + 2] for i in range(0, len(ciphertext), 2))
trigram_freq = Counter(ciphertext[i: i + 3] for i in range(0, len(ciphertext), 3))
quadgram_freq = Counter(ciphertext[i: i + 4] for i in range(0, len(ciphertext), 4))
for letter in range(26):
    if chr(letter + ord('A')) not in monogram_freq.keys():
        print(chr(letter + ord('A')))
print(bigram_freq)
print(trigram_freq)
print(quadgram_freq, '\n')


mapping = {'F': 'w', 'C': 't', 'S': 'e', 'K': 'h', 'Z': 'i'}
max_freq = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'd', 'l', 'u', 'c', 'm', 'f', 'y', 'w', 'g', 'p', 'b', 'v', 'k', 'x', 'q', 'j', 'z']
freq_mapping = get_mapping(max_freq, monogram_freq.copy())
freq_mapping['F'] = 'w'
print('monogram:', freq_mapping)

decrypted = substitution(ciphertext, freq_mapping)
print(decrypted)
print(list(decrypted[index: index + 7] for index in range(0, len(decrypted), 7)))
