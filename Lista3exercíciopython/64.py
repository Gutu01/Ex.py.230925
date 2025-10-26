codigo_cidade = []
veiculos_passeio = []
acidentes = []
menos_veicuolos = []
indice_transito = []

for i in range(5):
    codigo_cidade.append(int(input('\nDigite o código da cidade: ')))
    veiculos_passeio.append(int(input('Digite o número de veículos de passeio: ')))
    acidentes.append(int(input('Digite o número de acidentes de trânsito com vítimas: ')))
    
    indice_transito.append(acidentes[i]/veiculos_passeio[i])
    if veiculos_passeio[i] < 2000:
        menos_veicuolos.append(acidentes[i])

media_veiculos = (veiculos_passeio[0] + veiculos_passeio[1] +veiculos_passeio[2] + veiculos_passeio[3] + veiculos_passeio[4])/5
media_acidentes_menos_veiculos = sum(menos_veicuolos)/len(menos_veicuolos)

print(indice_transito)
print(f'O maior indice de acidentes de transito é de {}')
print(f'A média de veiculos de passeio é {media_veiculos}')
print(f'A média de acidentes nas cidades que tem menos de 2000 é {media_acidentes_menos_veiculos}')