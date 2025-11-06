# Isso a baixo é um tuplia. Tuplas são imutáveis, como uma constante em c.
# Se eu usasse um [] então seria uma lista e se fosse {} seria um dicionário

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

print(lanche[1])
print(lanche[-1])
print(lanche[-3:])
print(lanche[-1:-4-1:-1])

# A função enumerate em for retorna dois valores, o primerio é os itens da lista e o segundo é o indice do item 
# da lista
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

# O sorted faz a tupla aparecer em ordem
# Ela não é mudada por si só, ela só é
# exibida, nesse caso. Pode-se notar que 
# a tupla também é exibida como lista 
# por conta que tuplas é imutaveis
print(sorted(lanche))

# O mais na somas entre duas tuplas junta
# ambas e pode ser armazenada em outra
a = (3, 4, 6)
b = lanche + a
print(b)

# o 4 depois da vergula fala onde tem que
# começar a procurar, no caso ele vai
# procurar o número 3 e mostrar o index 
# dele na tupla.
print(b.index(3,4))

# Essa tupla é só para servir de exemplo que
# as tuplas podem receber vários varios dados
# de tiposs diferentes.
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)

# Isso é para mostrar que a única coisa que dá
# pra mudar em um tupla é apagando-a.
del(pessoa)