frase = input('Digite uma frase: ')

frase_maior = frase.upper()

print(f'Frase com letra maiúcula {frase_maior}')
print(f'Quantidade de caracteres com os espaços nas estremidades: {len(frase_maior)}')

sem_espaco = frase_maior.strip()

print(f'Quantidade de caracteres sem os espaços nas estremidades: {len(sem_espaco)}')