aluno = {'Nome' : '', 'idade' : '', 'curso' : ''}

aluno['nome'] = input('Digite o nome do aluno: ')
aluno['idade'] = int(input('Digite a idade do aluno: '))
aluno['curso'] = input('Digite o curso do aluno: ')

print(f'Nome: {aluno['nome']}')
print(f'Idade: {aluno['idade']}')
print(f'Curso: {aluno['curso']}')