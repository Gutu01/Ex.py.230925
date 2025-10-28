numero = input('Digite um número inteiro: ')

print(f'Seu número normal: {numero}')

print('Seu número invertido é: ', end='')

quantidade = len(numero)

for i in range(-1, -quantidade-1, -1):
    print(numero[i], end='')