lista = [1, 2, 3, 4, 5]

# O pop remove por posição, já o remove remove o item que se identifica
lista.pop(3)
lista.remove(1)
print(lista)

# O list cria uma lista que, com o range, vai de 4 à 10
valores= list(range(4, 11))

print(valores)

valores = [8, 4, 3, 2, 1, 9, 3 ,4]
# O sort deixa a lista em ordem
valores.sort()

print(valores)

# O reverse deixa a lista ordenada de forma inversa
valores.sort(reverse=True)

print(valores)

# Essa função vai adicionar o valor 69 na posição 3 e empurrar os demais
#para frente
valores.insert(3, 69) 

print(valores)

# Essa função, sem parametro, remove o último valor
valores.pop()

print(valores)

# A opção "a" não está fazendo uma cópia de valores, ela está fazendo
#uma ligação, logo, se eu mudar algo em valores, irá mudar em a também.
# Diferentemente de "b" que fazer uma cópia da lista inteira
a = valores
b = valores[:]

valores.append(6969)
print(a)
print(b)