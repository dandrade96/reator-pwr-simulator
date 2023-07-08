import time
import random
from reator import Reator
from comporta import Comporta
from sensor import Sensor
from atuador import Atuador

class CLP:
    def __init__(self, reator, comporta, sensor, atuador):
        self.reator = reator
        self.comporta = comporta
        self.sensor = sensor
        self.atuador = atuador

    def controlar_temperatura(self, temperatura_max):
        while True:
            temperatura_atual = self.sensor.medir_temperatura() # medir temperatura do reator

            self.reator.rotacao(random.uniform(10.0, 25.5)) # Rotaçao do motor do reator

            print("Temperatura atual do reator:", temperatura_atual)

            if temperatura_atual > temperatura_max:
                vazao_agua = 40  # Define uma vazão menor para diminuir a temperatura
            else:
                vazao_agua = 0 # mantem a vazão atual

            self.reator.atualizar_temperatura(vazao_agua)
            self.atuador.controlar_vazao(vazao_agua)
            
            # Aguarda um intervalo de tempo antes de verificar a temperatura novamente
            time.sleep(1)
            
# Criação dos objetos dos ambientes
volume_reator = 40  # Defina o volume do reator

reator = Reator(volume=volume_reator, temperatura_inicial=0) 
comporta = Comporta()
sensor = Sensor(reator)
atuador = Atuador(comporta)

# Define a temperatura máxima desejada (exemplo: 325)
# Para controle de temperatura mais preciso iniciamos uma maxima em 300 logo a temperatura não ultrapassa o nivel ideal
temperatura_maxima = 300 
# Criação do CLP
clp = CLP(reator, comporta, sensor, atuador)

# Inicia o controle de temperatura pelo CLP
clp.controlar_temperatura(temperatura_maxima)