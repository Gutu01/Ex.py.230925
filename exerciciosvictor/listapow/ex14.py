nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda falta: '))
faltas = int(input('Digite o número de faltas: '))

media = (nota1+nota2)/2
frequencia = faltas*100/300

if media >= 6:
    print('Você está acima da média!')
else:
    print('Você está abaixo da média!')

if frequencia >= 25:
    print(f'Sua porcentagem de faltas é de {frequencia:.2f}% e sua situação está insalubre!')
else:
    print(f'Sua porcentagem de faltas é de {frequencia:.2f}% e você está de boa, por enquanto...')