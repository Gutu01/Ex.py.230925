aprovado = 0

for i in range(10):
    print(f'\n{i+1}º aluno')
    notas1 = float(input(('1º Nota:')))
    notas2 = float(input(('2º Nota:')))
    notas3 = float(input(('3º Nota:')))
    notas4 = float(input(('4º Nota:')))

    media = (notas1+notas2+notas3+notas4)/4

    if media >= 7:
        aprovado = aprovado + 1

print(f'A quantidade de alunos que conseguir ser aprovados foram: {aprovado}')