import time
import random
from sensorComporta import SensorComporta
from atuadorComporta import AtuadorComporta
from comporta import Comporta
from sensorReator import SensorReator
from atuadorReator import AtuadorReator
from reator import Reator

class CLP:
    def __init__(self):

        # Reator
        self.reator = Reator(0)  # Temperatura inicial do reator
        self.sensorReator = SensorReator(self.reator)
        self.atuadorReator = AtuadorReator(self.reator)
        # Comporta
        self.comporta = Comporta(0)
        self.sensorComporta = SensorComporta(self.comporta)
        self.atuadorComporta = AtuadorComporta(self.comporta)

    def ligar_reator(self):
        i = 0
        while i < 5:
            print('Ligando o Reator...')
            if i == 4:
                print('Acionando rotação...')
            i += 1
            time.sleep(2)
        
        
    def ligar_rotacao(self):
        self.reator.ligar_rotacao(random.uniform(10.0, 25.5))
    
    def medir_temperatura(self):
        temperatura = self.sensorReator.medir_temperatura()
        print(f"Temperatura: {temperatura}°C")

        # Lógica de controle para ajustar a temperatura do Reator
        if temperatura > 290:
            self.resfriamento()
            self.atuadorReator.ajustar_temperatura(10)
        

    def resfriamento(self):
        escoamento = self.sensorComporta.escoamento()
        print(f"Escomaneto: {escoamento} Litros")
        if escoamento < 10:
            self.atuadorComporta.abrir_comporta(1)
        else:
            self.atuadorComporta.travar_comporta()

clp = CLP()
clp.ligar_reator()
while True:
    clp.ligar_rotacao()
    clp.medir_temperatura()
    clp.resfriamento()
    time.sleep(2)
    
