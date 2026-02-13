from classes import ContaBancario

nome = input('\nDê um nome a sua conta: ')
deposito1 = float(input('Digite o valor do primeiro depósito: '))
deposito2 = float(input('Digite o valor do segundo depósito: '))

conta = ContaBancario(nome)

conta.depositar(deposito1+deposito2)

print(f'Seu saldo atual é de R$ {conta.saldo}')

sacar = float(input('Digite o valor de saque: '))

if conta.saldo > 0 and sacar <= conta.saldo:
    conta.sacar(sacar)
    print(f'Seu saldo é de {conta.saldo}')
else:
    print('Não foi possível sacar, seu pobre!')