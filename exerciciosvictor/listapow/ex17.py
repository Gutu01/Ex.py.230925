par = 0
impar = 0

lista = []

for i in range(10):
    lista.append(int(input('Digite um número inteiro: ')))
    if lista[-1] % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"\nVocê digitou {par} números pares e {impar} número impares")