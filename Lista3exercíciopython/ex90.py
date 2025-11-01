lista_comissao = [0,0,0,0,0,0,0,0,0]

venda = float(input('Digite o valor da venda ou -1 para ver o: '))

comissao = venda*9/100

if comissao >= 200 and comissao <= 299:
    lista_comissao[0] += 1
elif comissao >= 300 and comissao <= 399:
    lista_comissao[1] += 1
elif comissao >= 400 and comissao <= 499:
    lista_comissao[2] += 1
elif comissao >= 500 and comissao <= 599:
    lista_comissao[3] += 1
elif comissao >= 699 and comissao <= 699:
    lista_comissao[4] += 1
elif comissao >= 700 and comissao <= 799:
    lista_comissao[5] += 1
elif comissao >= 800 and comissao <= 899:
    lista_comissao[6] += 1
elif comissao >= 900 and comissao <= 999:
    lista_comissao[7] += 1
elif comissao >= 1000:
    lista_comissao[8] += 1

while venda != -1:
    venda = float(input('Digite o valor da venda ou -1 para ver o: '))

    comissao = venda*9/100

    if comissao >= 200 and comissao <= 299:
        lista_comissao[0] += 1
    elif comissao >= 300 and comissao <= 399:
        lista_comissao[1] += 1
    elif comissao >= 400 and comissao <= 499:
        lista_comissao[2] += 1
    elif comissao >= 500 and comissao <= 599:
        lista_comissao[3] += 1
    elif comissao >= 699 and comissao <= 699:
        lista_comissao[4] += 1
    elif comissao >= 700 and comissao <= 799:
        lista_comissao[5] += 1
    elif comissao >= 800 and comissao <= 899:
        lista_comissao[6] += 1
    elif comissao >= 900 and comissao <= 999:
        lista_comissao[7] += 1
    elif comissao >= 1000:
        lista_comissao[8] += 1

print(f'Quantidade de pessoas com a comissão entre R$200 à R$299: {lista_comissao[0]}')
print(f'Quantidade de pessoas com a comissão entre R$300 à R$399: {lista_comissao[1]}')
print(f'Quantidade de pessoas com a comissão entre R$400 à R$499: {lista_comissao[2]}')
print(f'Quantidade de pessoas com a comissão entre R$500 à R$599: {lista_comissao[3]}')
print(f'Quantidade de pessoas com a comissão entre R$600 à R$699: {lista_comissao[4]}')
print(f'Quantidade de pessoas com a comissão entre 700 à R$799: {lista_comissao[5]}')
print(f'Quantidade de pessoas com a comissão entre 800 à R$899: {lista_comissao[6]}')
print(f'Quantidade de pessoas com a comissão entre R$900 à R$999: {lista_comissao[7]}')
print(f'Quantidade de pessoas com a comissão com R$1000 ou mais: {lista_comissao[8]}')