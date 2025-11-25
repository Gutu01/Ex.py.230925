lista = []
par = []
impar = []

numero = 1

while numero:
    numero = (int(input('Digite um número inteiro ou 0 para sair: ')))
    lista.append(numero)

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f'A lista original {lista}')
print(f'A lista de pares {par}')
print(f'A lista de impares {impar}')