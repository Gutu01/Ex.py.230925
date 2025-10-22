soma = 0
numero = int(input("Digite um número:"))
soma = soma +numero
print(f'Soma: {soma}')

while numero!=-999:
    numero = int(input("Digite um número:"))
    print(f'Soma: {soma}')
    if numero !=-999:
        soma = soma +numero

print(f'A soma dos números digtados formam {soma}')