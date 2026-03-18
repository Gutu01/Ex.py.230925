# with open ("teste.txt", "w") as arquivo:
#     arquivo.write("Boa noite cinderala.")

# arquivo = open("teste.txt")
# print('O principe foi aberto com sucesso.')

# print("teste.txt: ", arquivo.name)
# print("teste.txt: ", arquivo.mode)
# print("teste.txt: ", arquivo.closed)
# arquivo.close()
# print("teste.txt: ", arquivo.closed)

# with open("mateus.txt", "a") as arquivo:
#     arquivo.write("\nO Raphael só ligou o pc.")

# with open ("teste.txt", "r") as arquivo:
#     print("READLINE")
#     linha1 = arquivo.readline()
#     linha2 = arquivo.readline()
#     print(linha1)
#     print(linha2)

try:
    with open ("raphael.txt", "x") as arquivo:
        arquivo.write("\nO Raphael só liga o pc.\n")
        
except FileExistsError:
    print('Erro, o arquivo já existe.')