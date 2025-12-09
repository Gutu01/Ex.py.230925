while True:
    try:
        numero = int(input('Digite um número inteiro divisivel por 100:'))

        if numero % 100 == 0:
            print('Beleza!')
            break
        else:
            print('Seu número não é divisivel por 100')
    except ValueError:
        print('Valor inválido!')