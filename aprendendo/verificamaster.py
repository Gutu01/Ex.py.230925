entrada = input('Insira algo: ')

print('\nO tipo primitivo de entrada digitada é\n', type(entrada))

if entrada.isascii() == True:   
    print('É apenas da tabela ASCII: SIM')
else:
    print('É apenas da tabela ASCII: NÃO')

if entrada.isalnum() == True:   
    print('É/São apenas número(a) ou letra(s): SIM')
else:
    print('É/São apenas número(a) ou letra(s): NÃO')

if entrada.isnumeric() == True:   
    print('É/São apenas número(s): SIM')
else:
    print('É/São apenas número(s): NÃO')

if entrada.isalpha() == True:   
    print('É/São apenas letra(s): SIM')
else:
    print('É/São apenas letra(s): NÃO')

if entrada.isdecimal() == True:   
    print('É/São apenas decimal(s): SIM')
else:
    print('É/São apenas decimal(s): NÃO')

if entrada.isdigit() == True:   
    print('É/São apenas dígito(s): SIM')
else:
    print('É/São apenas dígito(s): NÃO')

if entrada.isidentifier() == True:   
    print('Pode(m) ser usado(s) para variável(s)/funções: SIM')
else:
    print('Pode(m) ser usado(s) para variável(s)/funções: NÃO')

if entrada.islower() == True:   
    print('É/São apenas minúsculo(s): SIM')
else:
    print('É/São apenas minúsculo(s): NÃO')

if entrada.isprintable() == True:   
    print('Pode ser(em) exibido(s)/printado(s) na tela: SIM')
else:
    print('Pode ser(em) exibido(s)/printado(s) na tela: NÃO')

if entrada.isspace() == True:   
    print('É/São espaço(s) em branco: SIM')
else:
    print('É/São espaço(s) em branco: NÃO')

if entrada.istitle() == True:   
    print('Todas as palavras começam com a letras maiúscula e o resto minúscula: SIM')
else:
    print('Todas as palavras começam com a letras maiúscula e o resto minúscula: NÃO')

if entrada.isupper() == True:   
    print('É/São apenas letra(s) maiúscula(s): SIM')
else:
    print('É/São apenas letra(s) maiúscula(s): NÃO')
