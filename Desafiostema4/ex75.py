# Usar fatiamento de tupla nesse exercício

brasileirao = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 'Botafogo', 'Fluminense', 'São paulo', 'Vasco da gama', 'Corinthians', 'atlético-MG', 'bragantino', 'grêmio', 'ceará SC', 'internacional', 'EC vitória', 'santos', 'juventude', 'fortaleza', 'sport recife')

print('\n', brasileirao[:5])
print(brasileirao[-4:])

# Encontrei um problema no sorted que ele prioriza as letras maiúsculo. Então tive que colocar todos com o começo com letra maiúscula
print(sorted(sorted(brasileirao)))