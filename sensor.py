class Sensor:
    def __init__(self, reator):
        self.reator = reator

    def medir_temperatura(self):
        return self.reator.obter_temperatura()