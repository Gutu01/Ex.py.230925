linhas = int(input('Digite o número de linhas: '))
colunas = int(input('Digite o númerod de colunas: '))

X = []

for i in range(colunas):
    l = []
    for p in range(linhas):
        l.append(int(input('Digite um número: ')))

    X.append(l)

for i in range(colunas):
    print(X[i])