caractere = input('Digite uma unica coisa: ')

""" O is é para verificar se algo é algo (is == é, em português). No caso ele erifica se a caractere é maiúscula, minuscula ou número"""
if caractere.isupper():
    print('Sua caractere é maiúscula')
elif caractere.islower():
    print('Sua caractere é minúscula')
elif caractere.isnumeric():
    print('Você digitou um número')
else:
    print('Você digitou outro simbolo!')