numeros = []

for i in range(5):
    numeros.append(float(input('Digite um número: ')))

soma = numeros[0] + numeros[1] + numeros[2] + numeros[3] + numeros[4]
media = (numeros[0] + numeros[1] + numeros[2] + numeros[3] + numeros[4])/5

print(f'A soma dos números é {soma:.2f}')
print(f'A média dos números é {media:.2f}')