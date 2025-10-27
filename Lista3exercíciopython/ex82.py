par = 0
impar = 0

for i in range(10):
    numero = int(input('Insira um número:'))

    if numero % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print(f'Quantidade de número pares digitados: {par}')
print(f'Quantidade de número impares digitados: {impar}')