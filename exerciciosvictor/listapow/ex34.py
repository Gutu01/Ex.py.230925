produtos = {123 : ['arroz', 5.50], 321 : ['agua', 10.10]}
            

codigo = int(input('Digite o código do produto: '))
quantidade = int(input('Digite a quantidade dele: '))

print(f'Você comprou {quantidade} unidades de {produtos[codigo][0]}. Sua conta ficará R${(produtos[codigo][1]*quantidade):.2f4}')