notas = []

for i in range(4):
    notas.append(float(input(f'Digite a {i+1}º nota: ')))

print('As notas são')

for i in range(4):
    print(f'{i+1}º nota: {notas[i]}')

media = (notas[0] + notas[1] + notas[2] + notas[3])/4

print(f'A média é {media:.2f}')