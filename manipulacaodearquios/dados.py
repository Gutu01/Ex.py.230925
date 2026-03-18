linha = []

while True:
    texto = input('Digite textos ou digite a palara sair para encerrar: ')
    if texto.lower() == 'sair':
        break
    linha.append(texto)


with open("meuarquivo.txt", "w") as dados:
    for i in linha:
        dados.write('\n'+ i)
    
with open('meuarquivo.txt', 'r') as dados:
    conteudo_linha = dados.read()
    print(conteudo_linha)