lista = []

numero = 1
while numero:
    numero = int(input('Digite um número inteiro ou 0 para sair:  '))
    
    if len(lista) == 0 or numero > lista[-1]:
        lista.append(numero)
    else:
        for i in range(len(lista)):
            if numero < lista[i]:
                lista.insert(i, numero)
                break
    
print(lista)