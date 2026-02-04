from mensagens import maiusculo
from operacoes import soma

letra = input('Digite apenas uma letra: ')
numero1 = float(input('Digite um numero: '))
numero2 = float(input('Digite outro numero: '))

print(maiusculo(letra))
print(f'e a soma dos seus número é de {soma(numero1, numero2)}')