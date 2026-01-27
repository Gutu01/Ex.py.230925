A = []
B = []
soma = []

print('1º Matrix:')
for i in range(2):
    l = []
    for p in range(3):
        l.append(int(input('Digite um número: ')))
    A.append(l)

print('2º Matrix:')
for i in range(2):
    l = []
    for p in range(3):
        l.append(int(input('Digite um número:')))
    B.append(l)

for i in range(2):
    l = []
    for p in range(3):
        l.append(A[i][p] + B[i][p])
    soma.append(l)

print(f'{soma[0]}\n{soma[1]}')