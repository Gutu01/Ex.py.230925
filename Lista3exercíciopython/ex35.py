desconto = 0

print('Escolha o tipo de carne')
print('1 - File Duplo')
print('2 - Alcatra')
print('3 - Picanha')
carne = int(input('Resposta: '))

quantidade = float(input('Digite a quantidade Kg: '))
print('1 - Cartão tabajara')
print('2 - Crédito')
print('3 - Débito')
pagamento = int(input('Resposta: '))

if pagamento == 1:
    desconto = 5/100

if carne == 1 and quantidade <= 5:
    print('\nCarne -> File Duplo')
    preco = 34.9
elif carne == 1 and quantidade > 5:
    print('\nCarne -> File Duplo')
    preco = 35.80
elif carne == 2 and quantidade <= 5:
    print('\nCarne -> Alcatra')
    preco = 44.9
elif carne == 2 and quantidade > 5:
    print('\nCarne -> Alcatra')
    preco = 46.8
elif carne == 3 and quantidade <= 5:
    print('\nCarne -> Picanha')
    preco = 66,9
elif carne == 3 and quantidade > 5:
    print('\nCarne -> Picanha')
    preco = 67.8

total = quantidade*preco

print(f'Quantidade -> Kg{quantidade:.2f}')
print(f'Total -> R${total:.2f}')

if pagamento == 1:
    print('Tipo de pagamento -> Cartão Tabajara')
    print(f'Valor do desconto -> {quantidade*carne*desconto}')
    print(f'Total com desconto -> {quantidade*carne*desconto}')
elif pagamento == 2:
    print('Tipo de pagamento -> Cartão de Crédito')
else:
    print('Tipo de pagamento -> Cartão de Débito')



