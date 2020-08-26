from ciphers import FiestelMixerCipher

fiestel_mixer = FiestelMixerCipher(9)
ciphertext = fiestel_mixer.encrypt(10)
print(ciphertext)
print(fiestel_mixer.decrypt(ciphertext))
