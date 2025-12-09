senha = '123'
falhas = 0

while True:
    tentativa = input('Digite a senha:')

    if tentativa == senha:
        print('Senha correta')
        break
    else:
        print('Senha incorreta!\n')

        falhas += 1
    
print(f'\nNúmero de falhas: {falhas}')