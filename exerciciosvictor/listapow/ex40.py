nomes = []
idades = []

while True:
    print('1 - Mais dados')
    print('0 - Sair')
    resposta = int(input('Resposta: '))

    if resposta == 0:
        break

    try:
        
        nome = input('Digite seu nome: ')

        nomes.append(nome)

        while True:
            idade = int(input('Digite a idade ou 0 para sair: '))

            if idade <= 0 or idade > 120:
                print('Idade inválida!')
            else:
                idades.append(idade)
                break

    except ValueError:
        print('Valor inválido')

print(nomes)
print(idades)