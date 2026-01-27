matrix = []

for i in range(2):
    l = []
    for p in range(2):
        l.append(int(input('Digite um número:')))
    
    matrix.append(l)

print(f'{matrix[0]}\n{matrix[1]}')