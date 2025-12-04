idade = 1

while idade:
    try:
        idade = int(input('Digite sua idade ou zero para sair: '))
        if idade > 0 and idade <= 11:

    except ValueError:
        print('Valor inválido!')