produto = {'nome': 'Sua mãe','preco': 'R$0,01','quantidade': '1'}

while True:
    print('1 - Nome ')
    print('2 - Preço ')
    print('3 - Quantidade ')
    resposta = int(input('Digite a opção para consultar: '))

    if resposta == 1 or resposta == 2 or resposta == 3:
        break

if resposta == 1:
    print(f'produto: {produto['nome']}')
elif resposta == 2:
    print(f'Preço: {produto['preco']}')
else:
    print(f'Produto: {produto['quantidade']}')