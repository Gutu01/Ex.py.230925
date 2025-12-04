numeros = []

for i in range(5):
    numeros.append(int(input(f'Digite {i+1}º número:')))

for i in range(-1, -5-1, -1):
    print(numeros[i])