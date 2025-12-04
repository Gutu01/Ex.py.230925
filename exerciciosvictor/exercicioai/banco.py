print("""1 - Crédito
2 - Débito
3 - Empréstimo
4 - Investimento
5 - Poupança""")

resposta = int(input('Resposta: '))

if resposta == 1:
    print('Saldo atual: R$69')

    credito = float(input('Digite um valor a depositar: '))
    total = 69 + credito

    print(f'\nSeu saldo atual R${total:.2f}')

elif resposta == 2:
    print('Saldo atual: R$69')

    debito = float(input('Digite o valor da conta a ser paga: '))
    total = 69 - debito

    print(f'Seu saldo atual é de R${total:.2f}')

elif resposta == 3:
    print('Saldo atual: R$69')

    emprestimo = float(input('Digite o valor de emprestimo: '))
    meses = int(input('Digite o valor de meses a pagar no emprestimo: '))
    total = 69 + emprestimo
    juros = emprestimo*(1+0.08)**meses
    total_com_juros = emprestimo +juros

    print(f'Saldo atual: R${total:.2f}')
    print(f'Com 8% ao mês, você pagará R${juros:.2f} de juros')
    print(f'Você está devendo R${total_com_juros:.2f}')

elif resposta == 4:
    print('Saldo atual: R$69')
    print('Saldo em investimento: R$69')

    investir = float(input('Digite o valor a ser investido: '))
    total = 69 + investir
    ganho = total * 2/100

    print(f'Saldo em investimento: R${total:.2f}')
    print(f'Com esse valor investido e rendendo 2% ao mês você ganhará R${ganho:.2f} por mês')

elif resposta == 5:
    print('Saldo atual: R$69')
    print('Saldo na poupança: R$69')

    poupar = float(input('Digite o valor a ser depositado na poupança: '))
    total = 69 + poupar
    ganho = total * 0.5/100

    print(f'saldo na poupança: R${total:.2f}')
    print(f'Com esse valor investido e rendendo 0.5% ao mês você ganhará R${ganho:.2f} por mês')

else:
    print('Valor inválido!')