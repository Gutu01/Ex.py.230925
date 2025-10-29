lista = [4.0,9.5,6.0,7.8,4.0]
print(lista)

# .insert adiciona o item 69 na posição 3 e empurra o resto pra frente
lista.insert(3, 69)

# O .remove remove o primeiro 4.0 que aparecer
lista.remove(4.0)

print(lista)

# O pop remove o número da lista na posição 2
lista.pop(2)

print(lista)

variavel = 'pocã'

# O .reverse inverte a lista
lista.reverse()
print(lista)

lista.sort()
print(lista)

for i in range(1, variavel):
    print(i)