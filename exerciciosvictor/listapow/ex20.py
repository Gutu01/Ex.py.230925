lista = []

numero = 1

while numero:
    try:
        numero = int(input('Digite um número inteiro ou 0 para sair: '))

        if numero == 0:
            break
        else:
            lista.append(numero)   

    except ValueError:
        print('Valor inválido')

print(f'A quantidade de número digitados foi de {len(lista)}')
print(f'A soma de todos eles foi de {sum(lista)}')
print(f'A média foi de {sum(lista)/len(lista)}')
print(f'O maior número foi {max(lista)}')
print(f'O menor número foi {min(lista)}') 