while True:
    try:
        valor = float(input("Digite o valor do custo de fábrica em R$: "))
        break
    except ValueError:
        print("valor inválido")

if valor > 0 and valor <= 50000:
    totoal = valor + valor*5/100
elif valor > 50000 and valor <= 75000:
    total = valor + valor*10/100 + valor*15/100
elif valor > 75000:
    total = valor + valor*15/100 + valor*20/100
else:
    print('Valor inválido!')

print(f'O custo ao consumidor ficará R${total:.2f}')