palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for i in range(len(palavras)):
    print(f'\nNa palavra {palavras[i]} temos', end="")
    for ii in range(len(palavras[i])):
        if palavras[i][ii] == 'a':
            print(' a', end="")
        elif palavras[i][ii] == 'e':
            print(' e', end="")
        elif palavras[i][ii] == 'i':
            print(' i', end="")
        elif palavras[i][ii] == 'o':
            print(' o', end="")
        elif palavras[i][ii] == 'u':
            print(' u', end="")