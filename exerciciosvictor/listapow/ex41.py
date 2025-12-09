while True:
    try:
        print('1 - Celsius')
        print('2 - Fahrenheit')

        resposta = int(input('Resposta: '))

        if resposta >= 1 and resposta <= 2:
            break
        else:
            print('\nValor inválido!')

    except ValueError:
        print('Valor inválido')
    
while True:
    try:
        temperatura = float(input('Insira o valor da temperatura: '))
        break
    except ValueError:
        print('Valor inválido')

if resposta == 1:
    convertido = temperatura * 9/5 +32
    print(f'Sua temperatura convertida é de {convertido}ºF')
else:
    convertido = (temperatura -32) * 5/9
    print(f'Sua temperatura convertida é de {convertido}ºC')