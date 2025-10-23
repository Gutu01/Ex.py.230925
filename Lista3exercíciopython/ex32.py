print('\n')
print('--='*6)
print('Caixa registradora')
print('--='*6)
print('Valor mínimo 10')
print('Valor máximo 600')
print('--='*6)
notas = int(input('\nDigite o valor de nota:'))

while notas > 600 or notas < 10:
    print('Número de notas inválido1\n')
    print('--='*6)
    print('Caixa registradora')
    print('--='*6)
    print('Valor mínimo 10')
    print('Valor máximo 600')
    print('--='*6)
    notas = int(input('\nDigite o valor de nota:')) 

if notas >= 100:
    notas_de_100 = int(notas/100)
    notas = notas - 100 * notas_de_100

    print(f'Notas de R$100: {notas_de_100}')

if notas >= 50:
    notas_de_50 = int(notas/50)
    notas = notas - 50 * notas_de_50

    print(f'Notas de R$50: {notas_de_50}')
if notas >= 10:
    notas_de_10 = int(notas/10)
    notas = notas - 10 * notas_de_10
    print(f'Notas de R$10: {notas_de_10}')

if notas >= 5:
    notas_de_5 = int(notas/5)
    notas = notas - 5 * notas_de_5
    print(f'Notas de R$5: {notas_de_5}')

if notas >= 1:
    print(f'Notas de R$1: {notas}')


