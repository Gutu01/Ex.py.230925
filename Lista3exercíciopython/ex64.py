codigo_cidade = []
veiculos_passeio = []
acidentes = []
menos_veicuolos = []
indice_transito = []

maior_indice = 0
maior_indice_cidade = 0
menor_indice = 0
menor_indice_cidade = 0

for i in range(5):
    codigo_cidade.append(int(input('\nDigite o código da cidade: ')))
    veiculos_passeio.append(int(input('Digite o número de veículos de passeio: ')))
    acidentes.append(int(input('Digite o número de acidentes de trânsito com vítimas: ')))

    indice_transito.append(acidentes[i]/veiculos_passeio[i])

    if i == 0:
        mairo_indice = indice_transito[0]
        menor_indice = indice_transito[0]
    
    if indice_transito[i] > maior_indice:
        maior_indice = indice_transito[i]
        maior_indice_cidade = codigo_cidade[i]

    if indice_transito[i] < menor_indice:
        menor_indice = indice_transito[i]
        menor_indice_cidade = codigo_cidade[i]

    if veiculos_passeio[i] < 2000:
        menos_veicuolos.append(acidentes[i])

media_veiculos = (veiculos_passeio[0] + veiculos_passeio[1] +veiculos_passeio[2] + veiculos_passeio[3] + veiculos_passeio[4])/5
media_acidentes_menos_veiculos = sum(menos_veicuolos)/len(menos_veicuolos)

print(f'\nO maior indice de acidentes de transito é de {max(indice_transito)} pertecente a cidade de código {maior_indice_cidade}')
print(f'O Menor indice de acidentes de transito é de {min(indice_transito)} pertecente a cidade de código {menor_indice_cidade}')
print(f'A média de veiculos de passeio é {media_veiculos}')
print(f'A média de acidentes nas cidades que tem menos de 2000 é {media_acidentes_menos_veiculos}')