biblioteca = {}

while escolha:

    print('\n1 - Cadastrar livro')
    print('2 - Buscar por nome')
    print('3 - Bucar por autor')
    print('4 - Buscar por gênero')
    print('5 - Listar todos')
    print('6 - Marcar como lindo')
    print('0 - Sair do sistema')
    escolha = int(input('Resposta: '))
    
    match escolha:
        case 1:
            