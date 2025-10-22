total_alunos = 3
matricula = []
sexo = []
altura = []
status = []
quantidade1 = 0
quantidade2 = 0

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

  print('Status físico')
  print('1 - Bom')
  print('2 - Regular')
  print('3 - Ruim')
    
  status.append(int(input('Resposta: ')))

  while status[i] > 3 or status[i] <1:
    print("""Status não existente\n""")
    print('Status físico')
    print('1 - Bom')
    print('2 - Regular')
    print('3 - Ruim')
    status[i] = int(input('Resposta: '))
    
  if altura[i] > 170 and sexo[i] == 2:
    quantidade1 = quantidade1 + 1
  elif sexo[i] == 1 and status[i] == 1:
    quantidade2 = quantidade2 + 1
    
print(f'Quantidade de alunas maiores que 1.7 metros: {quantidade1}')
print(f'Porcentagem de alunos masculinos que tem status físico bom: %{100*sexo.count(1)/quantidade2}')
    

    