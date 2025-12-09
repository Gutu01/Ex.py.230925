usuarios = []

while True:
    print('1 - Cadastrar usuário')
    print('2 - Listar usuário')
    print('3 - Remover usuário')
    print('0 - Sair')

    resposta = int(input('Resposta:'))

    match resposta:
        case 1:
            usuarios.append(input('Insira um usuário: '))
        case 2:
            print(usuarios)
        case 3:
            remover = input('Digite o usuario a ser removido')
            usuarios.remove(remover)
        case 0:
            break