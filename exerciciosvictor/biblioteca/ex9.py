from operacoes import soma, subtracao, multiplicacao

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

print(f'\nA soma deles é {soma(numero1, numero2)}')
print(f'A subtração deles é {subtracao(numero1, numero2)}')
print(f'A multiplicção deles é {multiplicacao(numero1, numero2)}')