pontos = 0
mais = 0

quantidade = int(input("""Digite a quantidade de livros você comprou no 
bimestre ou 0 para ver a sua pontuação e premição: """))

if quantidade == 1:
    pontos = 5
elif quantidade == 2:
    pontos = 15
elif quantidade == 3:
    pontos = 30
elif quantidade == 4:
    pontos = 60
elif quantidade >= 5:
    pontos = 80
else:
    print('\nvocê não tem nenhum brinde a ser resgatado')
    
if pontos >= 20 and pontos <= 35-1:
    print('\nVocê pode ganhar uma Eco Bag ou uma Caneta Personaliza!')
elif pontos >= 35 and pontos <= 65-1:
    print('\nVocê pode ganhar uma Eco Bag ou uma Caneta Personaliza!')
    print("""Você pode ganhar um livro (com valor máximo de R$30,00)
ou uma luminária de cabeceira""")
elif pontos >= 65:
    print('\nVocê pode ganhar uma Eco Bag ou uma Caneta Personaliza!')
    print("""Você pode ganhar um livro (com valor máximo de R$30,00)
ou uma luminária de cabeceira""")
    print("""Você pode ganahr 2 livros (com valor máximode R$100,00)
ou um power bank""")

print(f'\nVocê tem {pontos} pontos')