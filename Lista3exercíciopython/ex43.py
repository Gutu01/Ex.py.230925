moeda_01 = int(input('Digite a quantidade de moedas de R$0,01: '))
moeda_5 = int(input('Digite a quantidade de moedas de R$0,05: '))
moeda_10 = int(input('Digite a quantidade de moedas de R$0,10: '))
moeda_25 = int(input('Digite a quantidade de moedas de R$0,25: '))
moeda_50 = int(input('Digite a quantidade de moedas de R$0,50: '))
moeda_1 = int(input('Digite a quantidade de moedas de R$1,00: '))

total = moeda_01*0.01 + moeda_5*0.05 + moeda_10*0.10 + moeda_25*0.25 +moeda_50*0.5 + moeda_1

print(f'A quantidade total deu R${total:.2f}')