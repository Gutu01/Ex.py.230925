A = [
    [1, 2, 3],
    [4, 5, 6]
    ]

B = [
    [7, 8],
    [9, 10],
    [11, 12],
    ]

multiplicacao = []

for i in range(len(A)):
    l = []
    for p in range(len(A)):
        soma = 0
        for j in range(len(B)):
            soma += A[i][j] * B[j][p]
        l.append(soma)
    multiplicacao.append(l)

for i in range(2):
    print(f'{multiplicacao[i]}')      