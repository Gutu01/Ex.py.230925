dado = list()
pessoas = list()

print('1 - Começar')
print('0 - Sair')
resposta = int(input('Resposta: '))

while resposta:
    dado.append(input('Digite o nome de uma pessoa: '))
    dado.append(int(input('Digite o peso dela: ')))
    pessoas.append(dado[:])
    dado.clear()

    print('\n1 - Continuar')
    print('0 - Sair')
    resposta = int(input('Resposta: '))

print(f'Há {len(pessoas)} pessoas na lista')

for i in pessoas:
    print(i[1])