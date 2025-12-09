while True:
    try:
        estad = input(input('Digite S, C, D ou V: '))

        estado = estad.upper()
        if estado == 'S':
            print('Estado civil: Solteiro')
            break
        elif estado == 'C':
            print('Estado civil: Casado')
            break
        elif estado == 'D':
            print('Estado civil: Divorciado')
            break
        elif estado == 'V':
            print('Estado civil: Viúvo')
            break
        else:
            print('Valor inválido!')

    except ValueError:
        print('Valor inválido!')