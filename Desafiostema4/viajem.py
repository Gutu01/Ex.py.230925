km = float(input('Digite quantos Km vão ser a sua viajem de ônibus: '))

if km <= 200:
    custo = km*0.5
else:
    custo = km*0.45
print(f'Sua viajem custará R${custo:.2f}')