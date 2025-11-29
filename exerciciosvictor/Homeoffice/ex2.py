resposta = 1

while resposta:
    try:
        resposta = int(input('Digite sua idade ou 0 para sair: '))

        if resposta > 0 and resposta <= 11:
            print('Criança')
            break
        elif resposta > 11 and resposta <= 17:
            print('Adolescente')
            break
        elif resposta > 17 and resposta <= 59:
            print('Adulto')
            break
        elif resposta > 59:
            print('Idoso')
            break
        else:
            print('Valor incorreto')
    except ValueError:
        print('Valor incorreto')