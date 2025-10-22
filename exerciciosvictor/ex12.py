numeros = 0
par = 0

for i in range(5):
    numeros = int(input(f'{i+1}º Números: '))

    if numeros % 2 == 0:
        par = par +1

print(f'Números que foram pares: {par}')
