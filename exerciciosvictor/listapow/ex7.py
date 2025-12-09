usuario = "gutu"
senha = "123"

entrada_usuario = input('Digite o nome de usuário: ')
entrada_senha = input('Digite a senha: ')

if entrada_usuario == usuario and entrada_senha == senha:
    print('Acesso permitido!')
else:
    print('Acesso negado!')