p_horas = float(input('Digite o total de horas trabalhadas: '))
p_ganho_por_hora = float(input('Digite o quanto você ganha '))

p2_horas = float(input('\nDigite o total de horas trabalhadas: '))
p2_ganho_por_hora = float(input('Digite o quanto você ganha '))

salario1 = p_horas*p_ganho_por_hora
salario2 = p2_horas*p2_ganho_por_hora

if salario1 > salario2:
    print('A primeira professora ganha melhor!')
elif salario2 > salario1:
    print('A segunda professora ganha melhor!')
else:
    print('As duas professora ganham igualmente!')