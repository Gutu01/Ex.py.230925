print('Vamos ver o que você digitar é um triângulo')

reta1 = float(input('Insira o primeiro lado:'))
reta2 = float(input('Insira o segundo lado: '))
reta3 = float(input('Insira o terceiro lado: '))

if reta1 + reta2 > reta3:
    print('As retas formam um triângulo!\n')
else:
    print('As retas não formam um triângulo!\n')
