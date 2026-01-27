A = [
    [1, 2],
    [3, 4]
    ]

C = []

for i in range(2):
    l = []
    for p in range(2):
        l.append(A[i][p]*2)

    C.append(l)

print(f'{C[0]}\n{C[1]}')