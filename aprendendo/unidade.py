numero = input('Digite um número inteiro de 0 a 9999: ')
numero_ = int(numero)

if numero_ >= 0 and numero_ <= 9:
    print('Unidade(s):', numero[0])
elif numero_ >= 10 and numero_ <= 99:
    print('Unidade(s):', numero[1])
    print('Dezena(s):', numero[0])
elif numero_ >= 100 and numero_ <= 999:
    print('Unidade(s):', numero[2])
    print('Dezena(s):', numero[1])
    print('Centena(s):', numero[0])
elif numero_ >= 1000 and numero_ <= 9999:
    print('Unidade(s):', numero[3])
    print('Dezena(s):', numero[2])
    print('Centena(s):', numero[1])
    print('Milhar(es):', numero[0])
else:
    print('\nNúmero inválido!\n\n')