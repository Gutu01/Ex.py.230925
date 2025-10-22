sexo = 0

print('Digite')
print('1-Masculino')
print('2-Feminino')
sexo = int(input('Resposta:'))

while sexo > 2 or sexo < 1:
    print('\nSexo inválido!\n')

    print('Digite')
    print('1-Masculino')
    print('2-Feminino')
    sexo = int(input('Resposta:'))

altura = float(input('Digite sua altura: '))

if sexo == 1:
    print(f'Seu peso ideal é {72.7*altura-58:.2f}')
else:
    print(f'Seu peso ideal é {62.1*altura-44:.2f}')