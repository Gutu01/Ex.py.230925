# Esses são os teste de métodos de tipo. Existe de todos os tipos para cada tipo, mas os prin
# cipais estão aqui
entrada = input('Digite um número: ')

# Verifica se é um número, retorna verdadeiro ou falso
print('É um número:', entrada.isnumeric())

# Verifica se é letra
print('É letra:', entrada.isalpha())

# Verficar se é numero e letra
print('É numero e letra:', entrada.isalnum())

# Verifica se está só com letras maiusculas
print('Somente com letras maiusculas:', entrada.isupper())