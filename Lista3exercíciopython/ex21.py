salario = float(input('Digite seu salário: '))
comissao = float(input('Digite o valor das suas vendas: '))

print(f'Valor da comissão: R${comissao*4/100:.2f}')
print(f'Valor do salario final: R${comissao*4/100+salario}')