salario = float(input('Insira seu salário:'))

if salario > 1250:
    salario = salario + salario*10/100
else:
    salario = salario + salario*15/100
print(f'O seu salario com reajuste é R${salario:.2f}')