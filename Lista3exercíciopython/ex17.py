salario = float(input('Digite seu salário: '))

if salario <= 280 and salario > 0:
    salario_depois = salario + salario*20/100
    porcentagem = "20%"
elif salario > 280 and salario <= 700:
    salario_depois = salario + salario*15/100
    porcentagem = "15%"
elif salario > 700 and salario <= 1500:
    salario_depois = salario + salario*10/100
    porcentagem = "10%"
elif salario > 1500:
    salario_depois = salario + salario*5/100
    porcentagem = "5%"
elif salario <= 0:
    print('Você está desligado da empresa!\n')
    exit()


print("Salario antes do reajuste: ",salario)
print('Percentual do aumento: ', porcentagem)
print(f'Valor do aumento: {salario_depois-salario:.2f}')
print('Novo valor do salario: ', salario_depois)