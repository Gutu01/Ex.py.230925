from classes import Carro

modelo = input('Digite o modelo do carro: ')
carro1 = Carro(modelo)

for i in range(3):
    carro1.acelerar()
    carro1.freiar()