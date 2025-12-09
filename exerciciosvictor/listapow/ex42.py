permitido = '0123456789+-*./'

while True:
    try:
        expressao = input('Digite a expressão: ')

        for i in expressao:
            """ O not in verifica se o que está em permitido não está na caractere da expressao. """
            if i not in permitido:
                """ O raise ValueError força o código a parar e retorna o texto inserido indicando erro. """
                raise ValueError('valor inálido!')
            
        print(eval(expressao))

    except ValueError:
        print('Valor inválido')
