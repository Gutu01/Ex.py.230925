print('--='*11)
print('           Cardápio')
print('--='*11)
print('100 - Cachorro quente -> R$11,20')
print('101 - Ovo simples -> R$8,30')
print('102 - Bauru com ovo -> R$11,50')
print('201 - Refrigerante -> R$6,00')
print('202 - Suco -> R$7,50')
print('203 - Água Mineral -> R$4,70')
print('--='*11)

comida = int(input('Escolha uma comida: '))
bebida = int(input('Escolha uma bebida: '))

if comida == 100:
    preco_comida = 11.20
elif comida == 101:
    preco_comida = 8.30
else:
    preco_comida = 11.50

if bebida == 201:
    preco_bebida = 6
elif bebida == 202:
    preco_bebida = 7.5
else:
    preco_bebida = 4.7

total = preco_bebida+preco_comida

print(f'O preço R${total}')