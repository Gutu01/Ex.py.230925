celsius = float(input('Digite a temperatura em celsius: '))

if celsius < 15:
    print('Está frio')
elif celsius >= 15 and celsius < 31:
    print('O clima está agradável')
else:
    print('O clima está quente')