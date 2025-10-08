nome = input('Digite seu nome completo:')
nome_lista = nome.split()

print('Primeiro nome:', nome_lista[0])
# O index negativo pega o último item da lista 
print('Último nome:', nome_lista[-1])