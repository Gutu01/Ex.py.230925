#   Multiplique as matrizes A 2x3 * B 3x2 e C 2X5 * D 5X2 e some suas tabelas resultantates

A = [
    [55, 99, 14],
    [45, 47, 22]
    ]

B = [
    [69, 1],
    [21,25],
    [65,23]
    ]

C = [
    [36, 98, 44, 11, 25],
    [31, 19, 27, 14, 37]
    ]

D = [
    [99, 94],
    [50,9],
    [66, 17],
    [34, 52],
    [16,28]
    ]

X = []
Y = []
Z = []

for p in range(len(A)):
    L = []
    for i in range(len(A)):
        soma = 0
        for g in range(len(B)):
            soma += A[p][g] * B[g][i]
        L.append(soma)
    X.append(L)

for p in range(len(C)):   
    M = [] 
    for i in range(len(C)):
        soma = 0
        for g in range(len(D)):
            soma += C[p][g] * D[g][i]
        M.append(soma)    
    Y.append(M)

print(f'Multiplicação:\n\n{X[0]}\n{X[1]}')
print(f'\n{Y[0]}\n{Y[1]}')

for p in range(len(X)):
    l = []
    for i in range(len(X)):
        l.append(X[p][i] + Y[p][i])
    Z.append(l)

print(f'\nAdição:\n{Z[0]}\n{Z[1]}')