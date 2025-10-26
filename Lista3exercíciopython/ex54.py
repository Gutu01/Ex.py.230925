numeros = []
numero_especial = 0

numeros.append(int(input('Digite um número inteiro ou 0 para sair: ')))

while numeros[-1] != 0:
    numeros.append(int(input('Digite um número inteiro ou 0 para sair: ')))

tamanho_lista = len(numeros)

for i in range(tamanho_lista):
    if numeros[i] == 50:
        numero_especial = numero_especial + 1

print(f'Você digitou {numero_especial} vez o número 50')