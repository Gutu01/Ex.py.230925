from operacoes import validar

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

print(f'Seu primero número é positivo: {validar(numero1)}')
print(f'Seu segundo número é positivo: {validar(numero2)}')
