notas = []

notas.append(float(input('Digite uma nota ou -1 para sair do sistema: ')))

while notas[-1] != -1: 
    notas.append(float(input('Digite outra nota ou -1 para sair do sistema: ')))

notas.remove(-1)
print(notas)

for i in range(-1, -1, -1):
    print(i)