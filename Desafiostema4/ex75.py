numeros = []

for i in range(4):
    numeros.append(int(input('Digite um número inteiro: ')))

numero_tupla = (numeros[0], numeros[1], numeros[2], numeros[3],)

print(f'O número 9 aparece {numero_tupla.count(9)} veze (s)')
print(f'O primeiro valor 3 foi digitado na posição {numero_tupla.index(3)}')
print('a')