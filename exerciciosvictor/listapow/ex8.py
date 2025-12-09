import math

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

mes = int(input('Digite um número de 1 a 12 (correspondente ao mês): '))

print(f'Você escolheu o mês de {meses[mes-1]}, que corresponde ao ', end='')

if mes >= 1 and mes <= 3:
    print('1º semestre')
elif mes >= 4 and mes <= 6:
    print('2º semestre')
elif mes >= 7 and mes <= 9:
    print('3º semestre')
else:
    print('4º semestre')