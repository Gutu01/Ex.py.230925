entrada = input('Digite um número: ')

# Verifica se é um número, retorna verdadeiro ou falso
print('É um número:', entrada.isnumeric())

# Verifica se é letra
print('É letra:', entrada.isalpha())

# verficar se é numero e letra
print('É numero e letra:', entrada.isalnum())

# Verifica se está só com letras maiusculas
print('Somente com letras maiusculas:', entrada.isupper())