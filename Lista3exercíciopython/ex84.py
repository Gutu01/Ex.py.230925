lista = []

for i in range(10):
    lista.append(int(input('Digite um número inteiro: ')))

numero = int(input('Digite um novo número inteiro: '))

if numero in lista:
    print('Esse valor existe na lista')
else:
    print('Esse valor não existe na lista')