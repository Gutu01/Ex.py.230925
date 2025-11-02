notas = []

soma = 0

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