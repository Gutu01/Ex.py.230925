lista = []

soma = 0

for i in range(5):
    lista.append(float(input('Digite um número: ')))
    soma = soma + lista[i]

print(f'A soma do número é {soma}\n')

for i in range(5):
    print(lista[i])