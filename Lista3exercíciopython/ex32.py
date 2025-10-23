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

while notas >= 100:
    notas_de_100 = notas/100
    notas = notas - 100 * notas_de_100

    print(f'Notas de R$ {notas_de_100}')

while notas >= 50:
    notas_de_50 = notas/50
    notas = notas - 50 * notas_de_50
while notas >= 10:
    notas_de_10 = notas/10
    notas = notas - 10 * notas_de_10
while notas >= 5:
    notas_de_5 = notas/5
    notas = notas - 5 * notas_de_5

print('--='*6)
print('Troco do dinheiro')
print('--='*6)

if notas_de_100 > 0:
    print(f'Notas de R$100: {notas_de_100}')
if notas_de_50 > 0:
    print(f'Notas de R$50: {notas_de_50}')
if notas_de_10 > 0:
    print(f'Notas de R$10: {notas_de_10}')
if notas_de_5 > 0:
    print(f'Notas de R$5: {notas_de_5}')
if notas > 0:
    print(f'Notas de R$1:')