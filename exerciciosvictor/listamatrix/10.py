quantidade = [
            [1, 2],
            [3, 4]
            ]

preco = [
        [10.2, 30.4],
        [50.6, 60.7]
        ]

total = []

for i in range(2):
    l = []
    for p in range(2):
        l.append(quantidade[i][p] * preco[i][p])
    total.append(l)

print(f'{total[0]}\n{total[1]}')