nome = input('Digite seu nome completo:')
nome_lista = nome.split()

print('Primeiro nome:', nome_lista[0])
# O index negativo pega o último item da lista. O -1 pega o último, o
# -2 pega o penúltimo e assim por diante
print('Último nome:', nome_lista[-1])