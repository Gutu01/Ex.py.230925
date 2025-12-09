lista = []
multiplos = []

for i in range(3):
    lista.append(int(input('Digite um número:')))
    
    if lista[-1] % 3 == 0:
        multiplos.append(lista[-1])
    
print(f'Os multiplos de 3 são {multiplos}')