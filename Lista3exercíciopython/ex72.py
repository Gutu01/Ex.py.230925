notas = []

nome = input('Digite seu nome: ')

for i in range(7):
    notas.append(float(input(f'Digite a {i+1}º nota: ')))

print('Resultado final:')
print(f'Atleta: {nome}')
print(f'Melhor nota: {max(notas):.1f}')
print(f'Pior nota: {min(notas):.1f}')

notas.remove(max(notas))
notas.remove(min(notas))

media = (notas[0] + notas[1] + notas[2] + notas[3] + notas[4])/5

print(f'Média: {media:.2f}')