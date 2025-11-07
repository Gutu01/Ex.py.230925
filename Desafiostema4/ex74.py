from random import randint

numero1 = randint(0,10)
numero2 = randint(0,10)
numero3 = randint(0,10)
numero4 = randint(0,10)
numero5 = randint(0,10)

numeros = (numero1, numero2, numero3, numero4, numero5)

print(numeros)
print(f'O maior valor é {max(numeros)}')
print(f'O menor valor é {min(numeros)}')