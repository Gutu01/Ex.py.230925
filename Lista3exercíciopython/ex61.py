par = 0

for i in range(10):
    numero = int(input('Digite um número'))

    if numero % 2 == 0:
        par = par+1

print(f'você digitou {par} pares e {10-par} impares')