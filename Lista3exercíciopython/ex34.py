print('\n')
print('--='*8)
print('Preço dos combustíveis')
print('--='*8)
print('Gasolina - R$2,50')
print('Álcool - R$1,90')
print('--='*8)

quantidade = float(input('Quantidade de litros: '))

print('\nDigite')
print('1 - Gasolina')
print('2 - Álcool')
combustivel = int(input('Resposta:'))

while combustivel > 2 or combustivel < 1:
    print('Opção inválida\n')
    print('\nDigite')
    print('1 - Gasolina')
    print('2 - Álcool')
    combustivel = int(input('Resposta:'))

if combustivel == 1 and quantidade <= 20:
    total = 2.5*quantidade - 2.5*quantidade*3/100
    print(f'O preço total é de R${total:.2f} com 3% de desconto')
elif combustivel == 1 and quantidade > 20:
    total = 2.5*quantidade - 2.5*quantidade*5/100
    print(f'O preço total é de R${total:.2f} com 5% de desconto')
elif combustivel == 2 and quantidade <= 20:
    total = 1.9*quantidade - 1.9*quantidade*4/100
    print(f'O preço total é de R${total:.2f} com 4% de desconto')    
elif combustivel == 2 and quantidade > 20:
    total = 1.9*quantidade - 1.9*quantidade*6/100
    print(f'O preço total é de R${total:.2f} com 6% de desconto')
else:
    print('\n\nERRO\n\n')