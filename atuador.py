class Atuador:
    def __init__(self, comporta):
        self.comporta = comporta

    def controlar_vazao(self, vazao_desejada):
        self.comporta.ajustar_vazao(vazao_desejada)