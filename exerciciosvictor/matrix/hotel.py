#cpf, idade, telefone, nome, quarto, valor...

dados = [
        ['Nome', 'CPF', 'Idade', 'Telefone', 'Quarto', 'Valor']
        ]

while True:

    while True:
        print('1 - Adicionar dados ')
        print('0 - Fechar')
        resposta = int(input('Digite: '))
        
        if resposta == 1 or resposta == 0:
            break

    if resposta == 0:
        break

    linha = []

    for i in range(6):
        if i == 0:
            linha.append(input('Digite o seu nome: '))
        elif i == 1:
            linha.append(input('Digite seu CPF: '))
        elif i == 2:
            linha.append(int(input('Digite sua idade: ')))
        elif i == 3:
            linha.append(input('Digite seu telefone: '))
        elif i == 4:
            linha.append(int(input('Digite o número do quarto: ')))
        elif i == 5:
            linha.append(float(input('Digite o valor: ')))

    dados.append(linha)
    
for i in dados:
    print(i)