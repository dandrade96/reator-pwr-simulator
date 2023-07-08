class AtuadorComporta:
    def __init__(self, comporta):
        self.comporta = comporta

    def abrir_comporta(self, abertura):
        self.comporta.start(abertura)

    def travar_comporta(self):
        self.comporta.stop()