A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

B = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
    ]

C = []

for i in range(3):
    l = []
    for p in range(3):
        l.append(A[i][p] + B[i][p])
    C.append(l)

print(f'\n{C[0]}\n{C[1]}\n{C[2]}')