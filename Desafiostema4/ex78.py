lista = []
indice_maior = []
indice_menor = []

for i in range(5):
    lista.append(float(input('Digite um valor: ')))
    if i == 0:
        maior = menor = lista[i]

    if lista[i] >= maior:
        maior = lista[i]
    elif lista[i] <= menor:
        menor = lista[i]
        
for i in range(5):
    if lista[i] == maior:
        indice_maior.append(i)
    elif lista[i] == menor:
        indice_menor.append(i)

print(f'O maior número foi {maior:.2f} e está na posição {indice_maior}')
print(f'O menor número foi {menor:.2f} e está na posição {indice_menor}')