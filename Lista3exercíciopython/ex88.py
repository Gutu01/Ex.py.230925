troco_um = 0
troco_cinquenta = 0
troco_vinteecinto = 0
troco_dez = 0
troco_cinco = 0
troco_umcentavo = 0

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

troco = total - preco

if troco / 1:
    troco_um = troco/1
if troco-troco_um / 0.5:
    troco_cinquenta = troco%1/0.5
if troco-troco_um-troco_cinquenta / 0.25:
    troco_vinteecinto = troco%1.5/0.25
if troco / 0.1:
    troco_dez = troco%1.75/0.1
if 



if total >= preco:
    print('Produto comprado com sucesso!')
    print(f'O troco é { }')