palavra = input('Digite uma palavra com 10 letras: ')

vogais = palavra.count('a')
vogais = vogais + palavra.count('e')
vogais = vogais + palavra.count('i')
vogais = vogais + palavra.count('o')
vogais = vogais + palavra.count('u')

print(vogais)
