while True:
    numero = int(input("Digite um número maior que 0: "))
    
    if numero > 0:
        print("Você digitou:", numero)
    else:
        print("Número inválido!")

    # aqui vem a condição do "do while"
    if numero > 0:
        break