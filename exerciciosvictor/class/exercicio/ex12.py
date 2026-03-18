from classes import Pedido

pedido_top = Pedido()

for i in range(4):
    nome = input('Digite o nome do produto: ')
    preco = int(input('Digite o preço do produto: '))

    pedido_top.adicionar_item(nome,preco)

pedido_top.total()