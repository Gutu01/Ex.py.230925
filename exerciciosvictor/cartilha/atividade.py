# Aqui eu criei um lista vazia chamada produtos
produtos = []

# Aqui eu mostrei os tipos de variáveis como o inteiro que recebe apenas número inteiros, o float que recebe números com ponto flutuante,
# a string que recebe uma ou mais caracteres e o booleano que recebe verdadeiro ou falso.
print('Tipos de tipagem no python:')
variavel = 69
print(type(variavel))
variavel = 69.0
print(type(variavel))
variavel = '69'
print(type(variavel))
variavel = bool(69)
print(type(variavel))

# Aqui nessa parte eu peço para o usuário digitar um número ou sair do programa
print('\nDigite o valor do produto ou 0 para sair: ')
produtos.append(float(input('Resposta: ')))

# Essa estrutura abaixo verifica se a entrada do usuário é 0, se não for ele continua pedindo mais números.
while produtos[-1] != 0:
    print('\nDigite o valor do produto ou 0 para sair: ')
    produtos.append(float(input('Resposta: ')))

# Aqui eu somo todos os números da lista com o sum e depois eu exibo a soma para o usuários.
soma = sum(produtos)

print(f'\nA soma {soma:.2f}')

# Aqui eu peço o valor dinheiro dado ao vendedor
compra = float(input('Digite o valor do dinheriro, lembrando que o pastel é R$9.90: '))

# Aqui eu veri se o valor digitado é menor ou maior que 9.9, se for maior ou igual ele mostra o troco, caso contrário ele humilha o usuário
if compra >= 9.9:
    print(f'O troco restante é de R${compra-9.90:.2f}')
else:
    print('Sai daqui, Pobre!!')