usuario = input('Crie um nome de usuário: ')
senha = input('Crie uma senha: ')

while usuario == senha:
    print('A senha não pode ser a mesma do seu nome de usuário')

    usuario = input('\nCrie um nome de usuário: ')
    senha = input('Crie uma senha: ')