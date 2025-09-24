nome = input('Nome: ')
idade = int(input('Idade: '))

if idade >= 0 and idade <= 2:
    print(nome,"está com ", idade, "e pela tabela é considerado(a) um(a) bebê")
elif idade >= 3 and idade <= 11:
    print(nome,"está com ", idade, "e pela tabela é considerada uma criança")
elif idade >= 12 and idade <= 21:
    print(nome,"está com ", idade, "e pela tabela é considerado(a) um(a) jovem")
elif idade >= 22 and idade <= 64:
    print(nome,"está com ", idade, "e pela tabela é considerado(a) um(a) adulto(a)")
elif idade >= 65 and idade <= 100:
    print(nome,"está com ", idade, "e pela tabela é considerado(a) um(a) idoso(a)")
elif idade >= 101:
    print(nome,"está com ", idade, "e pela tabela é considerado(a) um(a) muito velhilho(a)")
else:
    print("Você não existe")