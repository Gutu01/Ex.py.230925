from classes import Produto

nomes = []
precos = []
descontos = []

for i in range(3):
    nomes.append(input('\nDigite o nome do produto: '))
    precos.append(float(input('Digite o preço do produto: ')))
    descontos.append(float(input('Digite o valor do desconto: ')))

desconto1 = Produto(nomes[0], precos[0])
desconto2 = Produto(nomes[1], precos[1])
desconto3 = Produto(nomes[2], precos[2])

print(f'\nO novo preço do produto {nomes[0]} é R${desconto1.aplicar_desconto(descontos[0])}')
print(f'O novo preço do produto {nomes[1]} é R${desconto2.aplicar_desconto(descontos[1])}')
print(f'O novo preço do produto {nomes[2]} é R${desconto3.aplicar_desconto(descontos[2])}')