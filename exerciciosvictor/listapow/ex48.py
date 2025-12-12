dias_semana = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']
vendas = []

for i in range(7):
    vendas.append(float(input(f'Digite o valor vendido na(o) {dias_semana[i]}: ')))

print(f'O total das vendas: R${sum(vendas)}')
print(f'A média das vendas: R${sum(vendas)/len(vendas)}')
print(f'A menor quantidade: R${min(vendas)}')
print(f'A maior quantidade: R${max(vendas)}')
print(f'A lista ordenada: {sorted(vendas)}')