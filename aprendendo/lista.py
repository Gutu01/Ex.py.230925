lista = [1, 2, 3, 4, 5]

# O pop remove por posição, já o remove remove o item que se identifica
lista.pop(3)
lista.remove(1)
print(lista)

# O list cria uma lista que, com o range, vai de 4 à 10
valores= list(range(4, 11))

print(valores)

valores2 = [8, 4, 3, 2, 1, 9, 3 ,4]
# O sort deixa a lista em ordem
valores2.sort()

print(valores2)

# O reverse deixa a lista ordenada de forma inversa
valores2.sort(reverse=True)

print(valores2)