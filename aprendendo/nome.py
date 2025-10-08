nome = input('Digite seu nome: ')
lista_nome = nome.split()

print('Seu nome em letras minúsculas:', nome.lower())
print('Seu nome em letras maiúsculas:', nome.upper())
print(f'Seu nome tem {len(nome.strip())} letras')
print(f'Seu primeiro nome tem {len(lista_nome[0])}')