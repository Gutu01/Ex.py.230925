meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

resposta = int(input('Digite o número do mês: '))

print(f'O mês {meses[resposta-1]} é ', end='')

if resposta == 12 or resposta == 1 or resposta == 2:
    print('verão')
elif resposta == 3 or resposta == 4 or resposta == 5:
    print('Outono')
elif resposta == 6 or resposta == 7 or resposta == 8:
    print('inverno')
elif resposta == 9 or resposta == 10 or resposta == 11:
    print('primavera')