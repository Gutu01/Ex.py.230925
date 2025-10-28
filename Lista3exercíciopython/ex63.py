numeros = []

numeros.append(int(input('Digite um número: ')))
numeros.append(int(input('Digite outro número: ')))

print(f'O maior número {max(numeros)}')
print(f'O menor número {min(numeros)}')
print(f'A soma dele é {numeros[0] + numeros[1]}')