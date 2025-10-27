saltos = []

nome = input('Digite seu nome: ')

if not nome:
    print('\n\nSaindo do programa')
    exit()

for i in range(5):
    saltos.append(float(input(f'{i+1}º salto (metros):')))

print(f'Atleta: {nome}\n')

for i in range(5):
    print(f'{i+1}º Salto: {saltos[i]}')

print(f'\nO maior salto foi de {max(saltos)} metros')
print(f'O menor salto foi de {min(saltos)} metros')

# O remove remove itens de uma lista

saltos.remove(max(saltos))
saltos.remove(min(saltos))

media = (saltos[0] + saltos[1] + saltos[2])/3

print(f'A média do resto dos saltos são {media:.2f} metros')