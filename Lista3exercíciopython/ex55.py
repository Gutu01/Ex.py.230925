numero = []

for i in range(20):
    numero.append(float(input(f'Digite o {i+1}º número:')))

maior = max(numero)
menor = min(numero)

print(f'O maior número foi {maior}')
print(f'O menor número foi {menor}')