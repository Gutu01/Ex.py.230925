print('Digite sua data de nascimento')
ano = int(input('Ano: '))

print('Digite o ano que está')
ano_esta = int(input('Ano: '))

total_anos = ano_esta-ano
total_meses = total_anos*12
total_dias = total_meses*30
total_semanas = total_meses*4

print('\nVocê tem')
print(f'{total_anos} anos')
print(f'{total_meses} meses')
print(f'{total_semanas} semanas')
print(f'{total_dias} dias')