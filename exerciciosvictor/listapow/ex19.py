nomes = []
index_maior = 0
index_menor = 0

quantidade = int(input('Digite a quantidade de nomes que você quer digitar: '))

for i in range(quantidade):
    nomes.append(input('Digite o nome: '))
    if len(nomes[-1]) > len(nomes[index_maior]):
        index_maior = nomes.index(nomes[-1])
    elif len(nomes[-1]) < len(nomes[index_menor]):
        index_menor = nomes.index(nomes[-1])


print(f'O nome com mais letras foi {nomes[index_maior]}')
print(f'O nome com menos letras foi {nomes[index_menor]}')