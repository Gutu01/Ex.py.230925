soma = 0

numero = int(input('Digite um número: '))

for i in range(1, numero+1):
    soma += i
    print(i)
    
print(soma)