frase = input('Digite uma frase: ')
quantidade_a_frase = frase.upper().replace('Ã','A').replace('Â','A').replace('Á','A').replace('À','A')

# O l antes do find faz pegar o primeiro 
print(quantidade_a_frase)
print('\nQuantidade de vezes que a letra "a" aparece:', quantidade_a_frase.count('A'))
print('A primeira letra "a" aparece na posição:', quantidade_a_frase.lfind('A'))
print('A última letra "a" aparece na posição:', quantidade_a_frase.rfind('A'))