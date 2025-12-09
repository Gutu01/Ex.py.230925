notas = []
acima_media = 0

for i in range(5):
    notas.append(float(input('Digite uma nota: ')))
    if notas[-1] >= 6:
        acima_media += 1
    
print(f'A média foi de {sum(notas)/5}')
print(f'Quantidade de notas acima da média {acima_media}')