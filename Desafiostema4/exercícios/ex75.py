par = 0

numeros = []

for i in range(4):
    numeros.append(int(input('Digite um número inteiro: ')))

numero_tupla = (numeros[0], numeros[1], numeros[2], numeros[3],)

print(f'O número 9 aparece {numero_tupla.count(9)} veze (s)')
if 3 in numero_tupla:
    print(f'O primeiro valor 3 foi digitado na posição {numero_tupla.index(3)}')
else:
    print('Não foi encontrado nenhum número 3')
for i in range(4):
    if numeros[i] % 2 == 0:
        par += 1
        
print(f'Você digitou {par} número(s) par(es)')