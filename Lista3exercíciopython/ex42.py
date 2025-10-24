lata = int(input('Digite a quantidade de latas de 350ml você quer comprar: '))
garrafa1 = int(input('Digite a quantidade de garrafas de 600ml você quer comprar: '))
garrafa2 = int(input('Digite a quantidade de garrafas de 2 litro você quer comprar: '))

total = lata*0.25 + garrafa1*0.6 + garrafa2*2

print(f'Total de litros a serem comprados {total:.2f}')