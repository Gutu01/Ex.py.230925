valor_hora = float(input("Digite quanto você ganha por hora: "))
horas_por_mes = int(input("Digite quantas horas você trabalha por mês: "))

valor_bruto = valor_hora * horas_por_mes

if valor_bruto <= 900 and valor_bruto > 0:
    ir = 0
elif valor_bruto > 900 and valor_bruto <= 1500:
    ir = 5
elif valor_bruto > 1500 and valor_bruto <= 2500:
    ir = 10
elif valor_bruto > 2500:
    ir = 20
else:
    print('\n\nSai daqui desempregado!\n\n')
    exit()

valor_bruto_ir = valor_bruto * ir/100
INSS = valor_bruto *10/100
FGTS = valor_bruto *11/100
total_desconto = valor_bruto_ir + INSS
salario_liquido = valor_bruto - (valor_bruto_ir + INSS)

print('\nSalário bruto: R$', valor_bruto)
print('Imposto de renda-', ir,'% (ou roubo): R$', valor_bruto_ir)
print('INSS-10% (também roubo): R$', INSS,)
print('FGTS-11%: R$', FGTS)
print('Total do desconto: R$', total_desconto)
print('Salário líquido: R$', salario_liquido)
