par = 0
impar = 0

numeros = []

for i in range(20):
    numeros.append(int(input('Digite um número inteiro: ')))
    
    if numeros[i] % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print(numeros)
print(f'Quantidade de número pares: {par}')
print(f'Quantidade de número impares: {impar}') 