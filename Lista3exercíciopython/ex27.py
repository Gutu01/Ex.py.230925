total_alunos = 3
matricula = []
sexo = []

for i in range(1,total_alunos):
    print(f'{i}º auno\n')
    matricula[i] = int(input('Digite sua matricula: '))
    print('Digite')
    print('1-Masculino')
    print('2-Feminino')
    sexo[i] = int(input('Resposta: '))
    
    while sexo[i] > 2 or sexo[i] < 1:
        print('\nSexo inválido!\n')
        print('Digite')
        print('1-Masculino')
        print('2-Feminino')
        sexo[i] = int(input('Resposta: '))
    