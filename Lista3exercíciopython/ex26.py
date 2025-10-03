valor = float(input('Digite o valor de aquisição: '))

if 0 < valor < 50:
    valor = valor + valor*45/100
elif valor >= 50:
    valor = valor + valor*30/100
else:
    print('Valor inválido!\n')

print(f'O valor de venda do produto é: R${valor:.2f}')
