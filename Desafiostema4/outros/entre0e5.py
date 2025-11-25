from random import randint
from time import sleep

computador = randint(0, 5)

numero = int(input('Escolha um número entre 0 e 5: '))

print('\nPensando...')
sleep(2)
print('\n')
print('--='*20)
if numero == computador:
    print('Parabéns, você acertou o número que eu estava pensando!')
else:
    print('Você errou o número que eu estava pensando :(')
print('--='*20)
sleep(2)
print(f'\nEu pensei no número {computador}')