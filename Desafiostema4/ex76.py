# Essa código tem o intuito de forçar a usar a tupla
# Qualquer item e preço, colocados na senquência, vão
#ser formatados
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 35)
print(' '* 7, 'LISTAGEM DE PREÇOS')
print('-' * 35)

for i in range(0, len(lista), 2):
    print(f'{lista[i]}', end="")
    print('.'*(25-len(lista[i])), end="")
    preco = str(lista[i+1])
    print('R$', ' '*(6-len(preco)),lista[i+1])

print('-'*35)