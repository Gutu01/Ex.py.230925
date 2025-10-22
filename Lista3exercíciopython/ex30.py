quilo = float(int(input('Digite o valor de quilos pescado: ')))

if quilo > 50:
    taxa = (quilo-50)*4

    print(f'Você foi taxado e pagará uma multa de R${taxa:.2f}')

else:
    print('Boa peixada!')