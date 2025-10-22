total_alunos = 3
matricula = []
sexo = []
altura = []
status = []

for i in range(total_alunos):

    print(f'\n{i+1}º auno\n')

    matricula.append(int(input('Digite sua matricula: ')))
    
    print('Digite')
    print('1-Masculino')
    print('2-Feminino')

    sexo.append(int(input('Resposta: '))) 
    
    while sexo[i] > 2 or sexo[i] < 1:
        print('\nSexo inválido!\n')
        print('Digite')
        print('1-Masculino')
        print('2-Feminino')
        sexo[i] = int(input('Resposta: '))
        
    altura.append(float(input('Digite a altura: ')))

    print("""Status físico
          1 - Bom
          2 - Regular
          3 - Ruim""")
    
    status.append(int(input('Resposta: ')))

    while status[i] > 3 or status[i] <1:
        print("""Status não existente\n""")
        print("""Status físico
          1 - Bom
          2 - Regular
          3 - Ruim""")
        status[i] = int(input('Resposta: '))
    
print(matricula,sexo)
    