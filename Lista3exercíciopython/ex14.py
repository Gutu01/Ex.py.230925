numero_conta = int(input('Digite o número da conta: '))
saldo = float(input('Digite o saldo da conta: '))
debito = float(input('Digite o valor a ser debitado: '))
credito = float(input('Digite o valor a ser creditado: '))

saldo_atual = saldo - debito + credito

if saldo_atual > 0:
    print('Seu saldo é positivo!\n')
elif saldo_atual < 0:
    print('Seu saldo é negativo!\n')
else:
    print('Seu saldo está zerado!\n')