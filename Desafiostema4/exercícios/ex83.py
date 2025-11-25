expressao = input('Digite uma expressão matemática com parenteses: ')

if expressao.count('(') == expressao.count(')'):
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')