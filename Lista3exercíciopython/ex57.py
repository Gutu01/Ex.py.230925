print('--='*10)
print(' '*10, 'Cardário')
print('--='*10)
print('1 - Bife Acebolado R$ 15,00')
print('2 - Lasanha R$ 25,00')
print('3 - Bife a Milanesa R$ 27,00')
print('4 - Bife a Vacalo R$ 24,00')
print('5 - Bobó de Frango R$ 24,00')
print('--='*10)
escolha = int(input('Escolha: '))

print('\nDeseja pagar os 10% do garçom?')
print('1 - Sim')
print('0 - Não')
gorjeta = int(input('Resposta:'))

if escolha == 1:
    prato = 15
elif escolha == 2:
    prato = 25
elif escolha == 3:
    prato = 27
elif escolha == 4 or escolha == 5:
    prato = 24

if gorjeta == 1:
    total = prato + prato*10/100
else:
    total = prato

print(f'O total ficou R${total:.2f}')