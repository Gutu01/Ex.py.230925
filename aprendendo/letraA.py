frase = input('Digite uma frase: ')
quantidade_a_frase = frase.upper().replace('Ã','A').replace('Â','A').replace('Á','A').replace('À','A')

print(quantidade_a_frase)
print('\nQuantidade de vezes que a letra "a" aparece:', quantidade_a_frase.count('A'))
print('A primeira letra "a" aparece na posição:', quantidade_a_frase.find('A'))
# O r antes do find faz com que dê para pegar a posição do último intem 
# selecionado da lista. Assim como no rstrip que tira os últimos espaços 
# desnecessários da frase
print('A última letra "a" aparece na posição:', quantidade_a_frase.rfind('A'))