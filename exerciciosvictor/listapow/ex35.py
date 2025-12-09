extrato = []

saldo = 0

while True:
    print('1 - Depósito')
    print('2 - Saque')
    print('3 - Extrato')
    print('0 - Sair')

    resposta = int(input('Resposta: '))

    match resposta:
        case 1:
            deposito = float(input('Digite o valor do depósito: '))

            saldo += deposito

            extrato.append(f'+ R${deposito}')
        case 2:
            saque = float(input('Digite o valor de saque: '))

            saldo -= saque

            extrato.append(f'- R${saque}')
        case 3: 
            print(f'Seu estrato: {extrato}')
            print(f'Valor em conta: R${saldo}')
        case 0: 
            break