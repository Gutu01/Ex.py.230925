print('Vamos ver a sua data de nascimento!')

dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

# O :02 faz com que complete com 2 até duas casas se não houver número
print(f'Sua data de nascimento é: {dia:02}/{mes:02}/{ano}')