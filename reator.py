class Reator:
    def __init__(self, volume, temperatura_inicial):
        self.volume = volume
        self.temperatura = temperatura_inicial

    def atualizar_temperatura(self, vazao_agua):
        self.temperatura -= vazao_agua

    def obter_temperatura(self):
        return self.temperatura

    def rotacao(self, rotacao):
        self.temperatura += rotacao