nome = []
autor = []
genero = []
ano = []
status = []

escolha = 1

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
            nome.append(input('\nDigite o nome do livro:'))
            autor.append(input('Digite o autor do livro: '))
            genero.append(input('Digite o gênero do livro: '))
            ano.append(input('Digite o ano que foi lançado o livro: '))

        case 2:
            print('\nDigite a escolha de busca')
            print('1 - Nome')
            print('2 - Autor')
            print('3 - Gênero')
            busca = int(input('Resposta:'))

            while busca != 1 and busca != 2 and busca != 3:
                print('\nDigite a escolha de busca')
                print('1 - Nome')
                print('2 - Autor')
                print('3 - Gênero')
                busca = input('Resposta:')  