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
# exibida, nesse caso.
print(sorted(lanche))