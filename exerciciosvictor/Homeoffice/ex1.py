resposta = 1
numero1 = 1
numero2 = 1

while resposta:
    try:
        print('\n1 - Somar')
        print('2 - Subtrair')
        print('0 - Sair do sistema')

        resposta = int(input('Resposta: '))

        if resposta >= 1 and resposta <=2:
            break        
        elif resposta == 0:
            exit()

    except ValueError:
        print('Valor inválido!')

while numero1:
    try:
        numero1 = int(input('\nInsira um número ou 0 para sair:'))

        if numero1 >0:
            break 
        elif numero1 == 0:
            exit()


        
    except ValueError:
        print('Valor inválido!')

while numero2:
    try:
        numero2 = int(input('\nInsira outro número ou 0 para sair: '))

        if numero2 >0:
            break    
        elif numero2 == 0:
            exit()
        
        
    except ValueError:
        print('Valor inválido!')

if resposta == 1:
    soma = numero1 + numero2
else:
    soma = numero1 - numero2

print(f'\nO resultado é {soma:.2f}')