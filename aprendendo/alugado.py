km = float(input('Digite a quantidade de Km percorridos: '))
dias = int(input('Digite a quantidade de dia que o carro foi alugado: '))

total = 60*dias + 0.15*km

print(f'O total a se pagar pelo carro alugado é R${total:.2f}')

