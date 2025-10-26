preco = float(input('Digite o valor do produto: '))

print('\nDigite uma opção de pagamento')
print('1 - À vista em dinheiro ou pix, recebe 10% de desconto')
print('2 - À vista no cartão de crédito, recebe 5% de desconto')
print('3 - Em duas vezes, preço normal de etiqueta sem juros')
print('4 - Em três vezes, preço normal de etiqueta mais juros de 10%')
resposta = int(input('Resposta: '))

if resposta == 1:
    preco = preco - preco*10/100
    print(f'O preço total fica R${preco:.2f}')
elif resposta == 2:
    preco = preco - preco*5/100
    print(f'O preço total fica R${preco:.2f}')
elif resposta == 3:
    preco = preco/2
    print(f'O preço total fica 2X de R${preco:.2f}')
elif resposta == 4:
    preco = (preco + preco*10/100)/3
    print(f'O preço total fica 3X de R${preco:.2f}')
else:
    print('ERROR')