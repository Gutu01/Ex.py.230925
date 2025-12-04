idade = 1

while idade:
    try:
        idade = int(input('Digite sua idade ou zero para sair: '))
        if idade > 0 and idade <= 11:
            print('Você é criança!')
            break
        elif idade > 11 and idade <= 17:
            print('Você é adolescente!')
            break
        elif idade > 17 and idade <= 59:
            print('Você é adulto!')
            break
        elif idade > 59 and idade <= 120:
            print('Você é Idoso!')
            break
        elif idade > 120:
            print('Valor inválido!')
        elif idade == 0:
            print('Saindo...')
            break
        else:
            print('Valor inválido!')
    except ValueError:
        print('Valor inválido!')