class Reator:
    def __init__(self, temperatura_inicial):
        self.temperatura = temperatura_inicial

    def atualizar_temperatura(self, escoamento):
        self.temperatura -= escoamento * 4.18

    def ligar_rotacao(self, rotacao):
        self.temperatura += rotacao