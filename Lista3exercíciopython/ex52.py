quantidade = 0
numero = int(input('Digite um número ou -1 para sair do código:'))
quantidade = quantidade+1

while numero != -1:
    numero = int(input('Digite um número ou -1 para sair do código:'))

    if numero != -1:
        quantidade = quantidade+1

print(f'A quantidade de números digitados é {quantidade}')