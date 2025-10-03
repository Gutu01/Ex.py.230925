for i in range(3):
    matricula[i] = int(input('Digite o número da matrícula: '))
    
    while True:
        sexo[i] = int(input('Digite 1 para Masculino ou 2 para feminino: '))

        if sexo[i] != 1 and sexo[i] != 2:
            print('\nSexo Inválido!\n')
        if sexo[i] == 1 or sexo[i] == 2:
            break
    