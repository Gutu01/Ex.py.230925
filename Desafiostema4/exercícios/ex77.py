palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for i in palavras:
    print(f'\nNa palavra {i} temos', end=" ")
    for ii in i:
        if ii in 'aeiou':
            print(ii, end=" ")