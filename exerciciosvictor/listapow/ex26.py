inteiros = []
positivos = []

for i in range(5):
    inteiros.append(int(input('Digite um número inteiro:')))

    if inteiros[-1] >= 0:
        positivos.append(inteiros[-1])
    
print(inteiros)
print(positivos)