linha = input('Digite varios valores com espaço entre eles: ')
lista_inteiros = []

separado = linha.split()

for i in separado:
    
    try:
        """Isso aqui verifica se é um número"""
        float(i)
        lista_inteiros.append(i)
    except ValueError:
        continue

print(lista_inteiros)