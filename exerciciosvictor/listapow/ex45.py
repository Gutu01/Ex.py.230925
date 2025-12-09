numeros = []

quantidade = 0
soma = 0

while True:
    numero = float(input('Digite um número ou 0 para sair: '))

    if numero == 0:
        break
    else:
        quantidade += 1
        soma += numero
        numeros.append(numero)

print(f'\nA quatidade de número é de {quantidade}')
print(f'A soma é de {soma:.2f}')
print(f'A média é de {soma/quantidade:.2f}')
print(f'O maior valor é de {max(numeros)}')
print(f'O menor valor é de {min(numeros)}')