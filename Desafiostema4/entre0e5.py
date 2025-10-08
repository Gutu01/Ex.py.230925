from random import randint

computador = randint(0, 5)

numero = int(input('Escolha um número entre 0 e 5: '))

if numero == computador:
    print('\nParabéns, você acertou o número que eu estava pensando!\n\n')
else:
    print('\nVocê errou o número que eu estava pensando :(\n\n')