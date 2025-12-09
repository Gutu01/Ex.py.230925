arquivos = ['123.txt']

resposta = input('Digite o nome do arquivo: ')

if resposta in arquivos:
    print('O arquivo é existe!')
else:
    print('O arquivo não existe!')