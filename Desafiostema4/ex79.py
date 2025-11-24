lista = []

numero = 1

while numero:
    numero = int(input('Digite um número ou 0 para sair: '))
    if numero in lista:
        print('\nEsse número já existe!\n')
    elif numero == 0:
        break
    else:
        lista.append(numero)
        
lista.sort()
print(lista)