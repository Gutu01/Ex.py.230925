altura = int(input('Digite sua altura em centimetro: '))
peso = float(input('Digite seu peso em Kg: '))

if altura <= 150 and altura >= 0:
    print('Altura = Ruim')
elif altura >= 151 and altura <= 160:
    print('Altura = Aceitável')
elif altura >= 161 and altura <= 165:
    print('Altura = Bom')
elif altura >= 166 and altura <= 170:
    print('Altura = Excelênte')
elif altura >= 171 and altura <= 175:
    print('Altura = Bom')
elif altura >= 176 and altura <= 180:
    print('Altura = Aceitável')
elif altura > 180:
    print('Altura = Ruim')
else: 
    print('Você não existe!')

if peso <= 45 and peso >= 0:
    print('Peso = Ruim')
elif peso >= 46 and peso <= 55:
    print('Peso = Bom')
elif peso >= 56 and peso <= 76:
    print('Peso = Excelênte')
elif peso >= 76 and peso <= 80:
    print('Peso = Bom')
elif peso > 80:
    print('Peso = Ruim')
else:
    print('Você não existe!')