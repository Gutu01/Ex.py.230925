divida = float(input('digite o valor da divida: '))

print('\nValor da Dívida - Valor dos Juros - Quantidade de parcelas - Valor da Parcela')
print(f'R${divida:.2f}       R$0       1       R${divida:.2f}')
print(f'R${divida+divida*10/100:.2f}       R${divida*10/100}       3       R${(divida+divida*10/100)/3:.2f}')
print(f'R${divida+divida*15/100:.2f}       R${divida*15/100}       6       R${(divida+divida*15/100)/6:.2f}')
print(f'R${divida+divida*20/100:.2f}       R${divida*20/100}       9       R${(divida+divida*20/100)/9:.2f}')
print(f'R${divida+divida*25/100:.2f}       R${divida*25/100}       12       R${(divida+divida*25/100)/12:.2f}')