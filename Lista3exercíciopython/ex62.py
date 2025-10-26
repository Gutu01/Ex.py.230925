fatorial = 1

numero = int(input('Digite um número para saber seu fatorial:'))

for i in range(1, numero+1):
    fatorial = fatorial *i

print(f'O fatorial do número {numero} é {fatorial}')


# Existe uma função em C que faz o fatorial, é da biblioteca
# import math e chamando o factorial você obtem o mesmo resultado,
# mas quis colocar assim para testar meus conhecimentos