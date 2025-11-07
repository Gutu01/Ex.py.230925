lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onde',
        'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('Digite um número inteiro entre 0 e 20: '))

while numero > 20 or numero < 0:
    numero = int(input('Valor incorreto!\nDigite um número inteiro entre 0 e 20: '))

print(f'O número você escolheu foi {lista[numero]}')