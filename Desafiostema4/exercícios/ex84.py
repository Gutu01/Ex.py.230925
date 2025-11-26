dado = list()
pessoas = list()

maior_peso = 1

print('1 - Começar')
print('0 - Sair')
resposta = int(input('Resposta: '))

while resposta:
    dado.append(input('Digite o nome de uma pessoa: '))
    dado.append(int(input('Digite o peso dela: ')))
    pessoas.append(dado[:])
    dado.clear()

    if pessoas[-1][1] > maior_peso:
        maior_peso = pessoas[-1][1]

    print('\n1 - Continuar')
    print('0 - Sair')

    resposta = int(input('Resposta: '))

print(f'\nHá {len(pessoas)} pessoas foram cadastradas')
print('\nLista das pessoas mais pesadas')

for i in pessoas:
    if i[1] == maior_peso:
        maior_peso = i[1]