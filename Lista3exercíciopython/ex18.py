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
# O f é o jeito de você chamar uma variável e depois é só coloca-la em {}
print(f'Imposto de renda-{ir}% (ou roubo): R${valor_bruto_ir:.2f}')
print(f'INSS-10% (também roubo): R${INSS:.2f}')
print(f'FGTS-11%: R${FGTS:.2f}')
print(f'Total do desconto: R${total_desconto:.2f}')
print(f'Salário líquido: R${salario_liquido:.2f}')
