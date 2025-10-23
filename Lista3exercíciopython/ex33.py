numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

print('\nEscolha uma operação\n')
print('1 - Par ou impar')
print('2 - Positivo ou negativo')
print('3 - Inteiro ou decimal')
resposta = int(input('Resposta:'))

while resposta > 3 or resposta < 1:
    print('\nResposta inválida\n')
    print('\nEscolha uma operação\n')
    print('1 - Par ou impar')
    print('2 - Positivo ou negativo')
    print('3 - Inteiro ou decimal')
    resposta = int(input('Resposta:'))

if resposta == 1:
    if numero1 % 2 == 0:
        print('O primeiro número é par')
    else:
        print('O primeiro número é impar')
    if numero2 % 2 == 0:
        print('O segundo número é par')
    else:
        print('O segundo número é impar')
if resposta == 2:
    if numero1 > 0:
        print('O primeiro número é positivo')
    elif numero1 < 0:
        print('O primerio número é negativo')
    else:
        print('O primeiro número é neutro')
    if numero2 > 0:
        print('O segundo número é positivo')
    elif numero2 < 0:
        print('O segundoo número é negativo')
    else:
        print('O segundo número é neutro')
if resposta == 3:
    if 
    