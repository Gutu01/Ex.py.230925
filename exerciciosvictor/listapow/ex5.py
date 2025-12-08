valor = float(input('Digite o valor da compra: '))

print('1 - A vista')
print('2 - Cartão (até 12x, com 3% de juros)')
print('3 - Boleto (até 12x, com 2% de juros)')
resposta = int(input('Resposta: '))

if resposta == 1:
    print(f'Sua compra ficará R${valor:.2f}')
elif resposta == 2:
    vezes = int(input('Digite a quantidade de parcelas: '))

    if vezes == 1:
        print(f'Sua compra ficará R${valor:.2f}')
    elif vezes >= 2 and vezes <=12:
        valor = valor + valor*3/100
        parcela = valor/vezes
        print(f'Sua compra ficará R${valor:.2f} em {vezes}x de {parcela:.2f}')   
    else:
        print('Parcela inválida!') 
    