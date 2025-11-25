numero1 = int(input('Digite um número:'))
numero2 = int(input('Digite um número:'))
numero3 = int(input('Digite um número:'))

if numero1 > numero2 and numero1 > numero3:
    print('O maior número é:', numero1)
elif numero2 > numero1 and numero2 > numero3:
    print('O maior número é:', numero2)
else:
    print('O maior número é:', numero3)

if numero1 < numero2 and numero1 < numero3:
    print('O menor número é:', numero1)
elif numero2 < numero1 and numero2 < numero3:
    print('O menor número é:', numero2)
else:
    print('O menor número é:', numero3)
