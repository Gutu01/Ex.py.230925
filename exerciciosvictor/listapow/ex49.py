nome = []
preco = []

for i in range(3):
    nome.append(input('Digite o nome: '))
    preco.append(float(input('Digite o preço: ')))

print(f'O produto mais caro é: {nome[preco.index(max(preco))]}')
print(f'O produto mais barato é: {nome[preco.index(min(preco))]:.2f}')
print(f'O preço médio é de: R${sum(preco)/len(preco)}')
print('Lista ordenada por ordem alfabética: \n')

for i, a in enumerate(sorted(nome)):
    print(f'{a}: R${preco[i]}')