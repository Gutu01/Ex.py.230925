numeros = []
par = 0

numeros.append(int(input('Digite qualquer número inteiro ou -999 para ver o resultado: ')))

while numeros[-1] != -999:
    numeros.append(int(input('Digite qualquer número inteiro ou -999 para ver o resultado: ')))

tamanho_lista = len(numeros)

print(tamanho_lista)

for i in range(tamanho_lista):
    if numeros[i] % 2 == 0:
        par = par +1

print(f'Você digitou {par} pares')