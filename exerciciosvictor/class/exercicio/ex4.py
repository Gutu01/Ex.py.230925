from classes import Retangulo

base1 = float(input('Digite a primeira base em m: '))
altura1 = float(input('Digite a primeira altura em m: '))
base2 = float(input('Digite a segunda base em m: '))
altura2 = float(input('Digite a segunda altura em m: '))

area1 = Retangulo(base1, altura1)
area2 = Retangulo(base2, altura2)

print(f'A área do primeiro retângulo é de {area1.area()} mº')
print(f'A área do segundo retângulo é de {area2.area()} mº')