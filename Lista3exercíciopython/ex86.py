salario = float(input('Digite o valor do salário: '))
financiamento = float(input('Digite o valor do financiamento: '))

if financiamento <= salario*5:
    print('Financiamento Concedido!')
else:
    print('Financiamento Negado!')

print('Obrigado por Consultar')