maior_palavra = ''
menor_palavra = ''
i = 0

frase = input('Digite uma frase: ')

separado = frase.split()

print(separado)
print(f'\nA quantidade de palavras é de: {len(separado)}')

for a in separado:
        
    if i == 0:
        maior_palavra = a
        menor_palavra = a
    else:
        if len(a) > len(maior_palavra):
            maior_palavra = a
        elif len(a) < len(menor_palavra):
            menor_palavra = a

    i += 1

print(f'A maior palara é {maior_palavra}')
print(f'A menor palavra é {menor_palavra}')