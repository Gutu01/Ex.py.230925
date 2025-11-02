notas = []

soma = 0
cima_media = 0
baixo_media = 0

notas.append(float(input('Digite uma nota ou -1 para sair do sistema: ')))

while notas[-1] != -1: 
    notas.append(float(input('Digite outra nota ou -1 para sair do sistema: ')))

notas.remove(-1)

print(notas)

for i in range(-1, -len(notas)-1, -1):
    soma += notas[i]
    print(notas[i])

print(f'A soma é: {soma:.2f}')

media = soma / len(notas)

print(f'A média é igual a: {media:.2f}')

for i in range(0, len(notas)):
    if notas[i] > media:
        cima_media += 1
    elif notas[i] < 7:
        baixo_media += 1

print(f'Valores acima da média: {cima_media}')
print(f'Valores acima da média: {baixo_media}')