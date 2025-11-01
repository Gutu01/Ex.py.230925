gasto = float(input('Digite o valor de m³ de água gasto: '))

total = 37.47
gasto = gasto - 5     

custo = [1.16, 6.46, 6.49, 6.55, 11.08]

if gasto > 0:
    if gasto > 5:
        total += 5*custo[0]
        gasto -= 5
    else:
        total = total + custo[0] * gasto
        gasto = 0
if gasto > 0:
    if gasto > 5:
        total += 5*custo[1]
        gasto -= 5
    else:
        total = total + custo[1] * gasto
        gasto = 0
if gasto > 0:
    if gasto > 5:
        total += 5*custo[2]
        gasto -= 5
    else:
        total = total + custo[2] * gasto
        gasto = 0
if gasto > 0:
    if gasto > 10:
        total += 10*custo[3]
        gasto -= 10
    else:
        total = total + custo[3] * gasto
        gasto = 0
if gasto > 0:
        total += gasto*custo[4]

print(f'Total de água a se pagar: R${total:.2f}')
print(f'total de esgoto a se pagar: R${total*80/100:.2f}')