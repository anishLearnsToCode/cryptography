class FiestelCipher:
    def __init__(self, rounds: list):
        self.rounds = rounds

    def encrypt(self, plain_number: int) -> list:
        for round in self.rounds:
            plain_number = round.encrypt(plain_number)
        return plain_number

    def decrypt(self, cipher_number):
        for round in self.rounds[::-1]:
            cipher_number = round.decrypt(cipher_number)
        return cipher_number
