class AtuadorReator:
    def __init__(self, reator):
        self.reator = reator

    def ajustar_temperatura(self, escoamento):
        self.reator.atualizar_temperatura(escoamento)
