nomes = []

for i in range(5):
    nomes.append(input(f'Digite o {i+1}º nome: '))

busca = input('Digite o nome para buscar: ')

if busca in nomes:
    print('Esse nome existe na lista')
else:
    print('Esse número não existe na lista')