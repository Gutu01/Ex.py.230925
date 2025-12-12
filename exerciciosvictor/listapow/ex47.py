nomes = []

comeca_letra = 0

while True:
    try:
        nomes.append(input('Digite um nome ou 0 para sair: '))

        if nomes[-1] == '0':
            nomes.remove('0')
            break
        else:
            continue

    except ValueError:
        print('Valor inválido')

print(f'Total de pessoas cadastradas {len(nomes)}')

letra = input('Digite uma letra para ver quantas pessoas começam com essa letra: ')

for i in nomes:
    if i[0].upper() == letra.upper():
        comeca_letra += 1

print(f'A quantidade de pessoas que começam com a letra {letra} são: {comeca_letra}')
print(f'A lista em ordem alfabetica é {sorted(nomes)}')