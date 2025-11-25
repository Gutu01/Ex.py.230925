# Usar fatiamento de tupla nesse exercício

brasileirao = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 'Botafogo', 'Fluminense', 'São Paulo', 'Vasco Da Gama', 'Corinthians', 'Atlético-MG', 'Bragantino', 'Grêmio', 'Ceará SC', 'Internacional', 'EC Vitória', 'Santos', 'Juventude', 'Fortaleza', 'Sport Recife')

print('\n', brasileirao[:5])
print(brasileirao[-4:])

# Encontrei um problema no sorted que ele prioriza as letras maiúsculo. Então tive que colocar todos com o começo com letra maiúscula
print(sorted(sorted(brasileirao)))

if 'chapecoense' in brasileirao:
    print(brasileirao.index('Chapecoense'))