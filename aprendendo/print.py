nome = input('Digite seu nome: ')

# Com isso eu consigo alinhar onde eu quisar o nome ou mesmo limitar
# o número de caracteres.
print(f'Nome com 20 espaços: {nome:20}')
print(f'Nome na direita: {nome:>20}')
print(f'Nome na esquerda: {nome:<20}')
print(f'Nome no centro: {nome:^20}')
print(f'Nome coberto de igual: {nome:=^20}')