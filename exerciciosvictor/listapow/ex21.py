vogais = 0

frase = input('Digite uma frase: ')

frase_maior = frase.upper()

for i in frase_maior:
    if i in 'AEIOU':
        vogais += 1

print(f'A quantidade de caracteres que ela tem é de {len(frase)}')
print(f'A quantidade de espaços que ela tem é de {frase.count(' ')}')
print(f'A quantidade de vogais nela são de {vogais}')
