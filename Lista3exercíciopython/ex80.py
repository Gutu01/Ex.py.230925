idade = []
altura = []

for i in range(5):
    idade.append(int(input('Digite sua idade: ')))
    altura.append(int(input('Digite sua altura: ')))

print('Idades: ')

for i in range(-1, -5-1, -1):
    print(idade[i], end=', ')

print('Alturas: ')

for i in range(-1, -5-1, -1):
    print(altura[i], end=', ')