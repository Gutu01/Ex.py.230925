palavra_antes = input('Digite uma palavra com 10 letras: ')

palavra = palavra_antes.lower()
vogais = palavra.count('a')
vogais = vogais + palavra.count('e')
vogais = vogais + palavra.count('i')
vogais = vogais + palavra.count('o')
vogais = vogais + palavra.count('u')

total = 10 - vogais

print(f'Sua palavra tem {total} vogais')
