print('--='*10)
print(' '*9,'Cafeteira')
print('--='*10)
print('1 - Café normal -> R1,05')
print('2 - Café expresso -> R$1,52')
print('3 - Capuccino -> R$2,17')
print('4 - Mocaccino -> R$2,36')

resposta = int(input('Digite a sua resposta:'))

if resposta == 1:
    preco = 1.05
elif resposta == 2:
    preco = 1.52
elif resposta == 3:
    preco = 2.17
elif resposta == 4:
    preco = 2.36
else:
    print('Valor inválido!')

um_real = int(input('\nDigite a quantidade de moedas de R$1,00: '))
cinquenta_real = int(input('Digite a quantidade de moedas de R$0,50: '))
vinteecinco_real = int(input('Digite a quantidade de moedas de R$0,25: '))
dez_real = int(input('Digite a quantidade de moedas de R$0,10: '))
cinco_real = int(input('Digite a quantidade de moedas de R$0,05: '))
zeroum_real = int(input('Digite a quantidade de moedas de R$0,01: '))

total = um_real + cinquenta_real*0.5 + vinteecinco_real*0.25 + dez_real*0.10 + cinco_real*0.05 + zeroum_real*0.01

