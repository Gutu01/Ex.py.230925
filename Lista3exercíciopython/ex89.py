gasto = float(input('Digite o valor de m³ de água gasto: '))

total = 37.47
gasto = gasto - 5     

custo = [1.16, 6.46, 6.49, 6.55, 11.08]

if gasto > 0:
    if gasto > 5:
        total += custo[0]
    else:
        total *= gasto
        gasto -= gasto
if gasto > 0:
    if gasto > 5:
        total += custo[1]
    else:
        total *= gasto
        gasto -= gasto
if gasto > 0:
    if gasto > 5:
        total += custo[2]
    else:
        total *= gasto
        gasto -= gasto
if gasto > 0:
    if gasto > 5:
        total += custo[3]
    else:
        total *= gasto
        gasto -= gasto
if gasto > 0:
    if gasto > 5:
        total += custo[4]
    else:
        total *= gasto
        gasto -= gasto

