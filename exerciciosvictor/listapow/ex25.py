produtos = {}
total= 0

quantidade = int(input('Digite a quantidade de produtos a serem cadastrados: '))

for i in range(quantidade):
    produto = input('Produto: ')
    preco = float(input('Preço: '))

    total += preco

    produtos[produto] = preco
    
    if i == 0:
        maior_preco = preco
        menor_preco = preco
        produto_mais_caro = produto
        produto_menos_caro = produto
    elif preco > maior_preco:
        maior_preco = preco
        produto_mais_caro = produto
    elif preco < menor_preco:
        menor_preco = preco
        produto_menos_caro = produto

print(f'O total fica R${total:.2f}')
print(f'O produto mais caro foi {produto_mais_caro}')
print(f'O produto mais barato foi {produto_menos_caro}')