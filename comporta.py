class Comporta:
    def __init__(self, abertura):
        self.escoamento = 0

    def start(self, abertura):
        self.escoamento += abertura * 10

    def stop(self):
        self.escoamento