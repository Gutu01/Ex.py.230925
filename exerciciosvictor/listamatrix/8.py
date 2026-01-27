A = [
    [1, 2],
    [3, 4]
    ]

B = [
    [5, 6],
    [7, 8]
    ]

multiplicacao = []

for q in range(2):
    l = []
    for i in range(2):
        soma = 0
        for p in range(2):
            soma += A[q][p] * B[p][i]
        l.append(soma)
    multiplicacao.append(l)

print(f'{multiplicacao[0]}\n{multiplicacao[1]}')