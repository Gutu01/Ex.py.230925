print('Informe os três lados de um triângulo')

lado1 = float(input('Lado 1:'))
lado2 = float(input('Lado 2:'))
lado3 = float(input('Lado 3:'))

if lado1 == lado2 == lado3:
    print('Seu triângulo é equilátero!\n')
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print('Seu triângulo é isósceles!\n')
else:
    print('Seu triângulo é escaleno!\n')