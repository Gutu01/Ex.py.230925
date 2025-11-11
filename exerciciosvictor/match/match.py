import random 

for i in range(15):

    numero = random.randint(1, 5)
    if numero == 1:
        compara = 'A'
    elif numero == 2:
        compara = 'B'
    elif numero == 3:
        compara = 'C'
    elif numero == 4:
        compara = 'D'
    elif numero == 5:
        compara = 'E'

    questao = input('\nDigite a alternativa da questão (de A à E): ')
    alternativa = questao.upper()

    if alternativa == compara:
        opcao = True
    else:
        opcao = False

    match opcao:
        case True:
            print('Questão certa')
        case False:
            print('Questão errada!')