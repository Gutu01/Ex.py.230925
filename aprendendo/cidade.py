cidade = input('Digite o nome da sua cidade: ')
lista_cidade = cidade.split()

if 'SANTO' in lista_cidade[0].upper():
    print('\nSua cidade começa com a palavra santo.\n\n')
else:
    print('\nSua cidade não começa com a palavra santo.\n\n')