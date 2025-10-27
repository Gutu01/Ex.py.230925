peso = float(input('Digite o peso da encomenda (em gramas):'))

if peso <= 500 and peso > 0:
    preco = 1.1
elif peso > 500 and peso <= 2000:
    preco = 2.2
elif peso > 2000 and peso < 10000:
    preco = 3.7
elif peso > 10000:
    preco = 5 + ((peso-10000)*3.8)
else:
    print('Valor inválido!')

print(f'O preço da encomenda ficará R${preco:.2f}')