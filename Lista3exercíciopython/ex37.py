pao = int(input('Digite a quantidade de Pães vendidos: '))
broa = int(input('Digiet a quantidade de broas vendidos: '))

total = pao*1 + broa*3.5
poupanca = total*10/100

print(f'Total arrecadado das vendas R${total:.2f}')
print(f'Total para ir na poupança R${poupanca:2f}')