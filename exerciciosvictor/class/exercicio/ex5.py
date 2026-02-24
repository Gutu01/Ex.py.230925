from classes import Carro

modelo = input('Digite o modelo do carro: ')

carrotop = Carro(modelo)

for i in range(3):
    acelerar = float(input('Digite o valor da aceleração: '))

    carrotop.acelerar(acelerar)

    freiar = float(input('Digite o valor do freio: '))

    carrotop.freiar(freiar)