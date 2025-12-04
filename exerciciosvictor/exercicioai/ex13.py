numero = []

for i in range(5):
    numero.append(float(input(f'Digite o {i+1}: ')))

print(f'O maior número é: {max(numero)}')
print(f'O menor número é: {min(numero)}')