from animal import Animal

nome = input('Digite o nome do animal: ')
peso = float(input('Digite o peso do animal em kg: '))
raca = input('Digite o raça do animal: ')

animal_top = Animal(nome, peso, raca)

while True:

    print('\nDigite a opção')
    print('1 - Nadar')
    print('2 - Voar')
    print('3 - Pular')
    print('0 - Sair')
    resposta = int(input('Resposta: '))

    if resposta == 1:
        animal_top.nadar()
    elif resposta == 2:
        animal_top.voar()
    elif resposta == 3:
        animal_top.pular()
    elif resposta == 0:
        break
    else:
        print('\n\nTente novamente')