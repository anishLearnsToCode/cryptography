class FiestelMixerCipher:
    def __init__(self, key: int):
        self.key = key

    def encrypt(self, number: int) -> int:
        return number ^ self.key

    def decrypt(self, number: int) -> int:
        return self.encrypt(number)
