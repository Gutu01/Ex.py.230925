A = int(80000)
B = int(200000)
i = 2
print('\n1º ano')
print('Cidade A -> 80000 habitantes')
print('Cidade B -> 200000 habitantes')

while A <= B :
    print(f'\n{i}º ano')
    i = i+1
    A = A+A*3/100
    B = B+B*1.5/100
    print(f'Cidade A -> {int(A)} habitantes')
    print(f'Cidade B -> {int(B)} habitantes')