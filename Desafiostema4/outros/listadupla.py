galera = list()
dado = list()
total_maior = total_menor = 0

#   Aqui basicamente eu coloco dois itens separados no dado e depois junto eles com uma cópia em galera. Logo em seguida
#limpo a lista para haver mais itens a serem copiados. 
for c in range(0,3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        total_menor += 1

print(f'Temos {total_maior} pessoas maiores de idade')
print(f'Temos {total_menor} pessoas menores de idade')