frase = input('Digite uma frase: ')

separado = frase.split()

print(separado)
print(f'Quantidade de palavras {len(separado)}')
print(f'A palavra com mais letars {max(separado)}')