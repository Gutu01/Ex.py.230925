numeros = []
resposta = 1


while resposta:
    try:
        numero = float(input('Digite um número: '))
        numeros.append(numero)
    except ValueError:
        print('Valor inválido!')

num_max = max(numeros)
num_min= min(numeros)

print(f'O Maior número é {num_max:.2f}')
print(f'O Maior número é {num_min:.2f}')