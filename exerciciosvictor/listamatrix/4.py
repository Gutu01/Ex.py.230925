matrix1 = []
matrix2 = []
soma = []

print('1º Matrix:\n')
for i in range(2):
    l = []
    for p in range(2):
        l.append(int(input('Digite um número:')))
    matrix1.append(l)

print('2º Matrix:\n')
for i in range(2):
    l = []
    for p in range(2):
        l.append(int(input('Digite um número: ')))
    matrix2.append(l)

for i in range(2):
    l = []
    for p in range(2):
        l.append(matrix1[i][p] + matrix2[i][p])
    soma.append(l)

print(f'\n{soma[0]}\n{soma[1]}')