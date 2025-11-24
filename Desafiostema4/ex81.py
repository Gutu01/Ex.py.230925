lista = []

numero = 1

while numero:
    numero = int(input('Digite um número ou 0 para sair:'))
    lista.append(numero)

print(f'Foram digitados {len(lista)} números')
lista.sort(reverse = True)
lista.remove(0)
print(f'Lista decrescente{lista}')
if 5 in lista:
    print('Existe o número 5 na lista!')
else:
    print('O número 5 não existe na lista!')