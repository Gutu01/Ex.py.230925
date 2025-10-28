salario = 1200

conta1 = 200
conta2 = 120

contas_com_juros = conta1 + conta1*10/100 + conta2 + conta2*10/100
resto = salario - contas_com_juros
print(f'João terá que pagar R${contas_com_juros} de contas por conta dos juros')
print(f'Restará R${resto} do salário de joão')