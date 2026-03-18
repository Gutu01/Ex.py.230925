from biblioteca import Biblioteca

livros = []

while True:

    try:
        print('1 -  Adicionar livro')
        print('2 - Listar liros')
        print('3 - Fazer emprestimo')
        print('4 - Realizar devolução')
        print('5 - Pesquisar livro')
        print('0 - Sair')
        resposta = int(input('Insira sua escolha: '))

        if resposta < 0 or resposta > 5:
            print('\nOpção inválida!\n')
            continue
        
#   O continue pula todo código que tem no loop e volta pro início

    except ValueError:
        print('\nValor inválido\n')
        continue

    match resposta:

        case 1:
            nome = input('Digite o nome do livro: ')
            livro = Biblioteca(nome)    
            livros.append(livro)

        case 2:
            print('\nlista dos livros:')
            for i in livros:
                print(i._nome)
            print()
            
        case 3:
            pesquisa = input('\nDigite o nome do livro: ')

            if pesquisa in livros:

        
        

        



# nome = input('Digite o nome do livro: ')

# livro1 = Biblioteca(nome)

# livro1.emprestar()
# livro1.devolver()
# livro1.devolver()
# livro1.emprestar()
# livro1.emprestar()

# livro1.status()
