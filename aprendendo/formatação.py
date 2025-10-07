# Da parte e nem voar em diante foi adicionado posteriormente

frase = 'A Vaca Não Sabe Nadar e Nem Voar'

# Mostra a letra "v", pois o frase[2] vê a posição na memória onde está
print(frase[2])

# A mesma coisa para frase[2:5], mostrará "vac", não "vaca" completo
# pois o último número vai até o anterior a ele na posição
print(frase[2:5])

print(frase[2:6])
# Agora sim está certo   

print(frase[2:21])
# Agora eu "fatiei" até o final, porém o arrey selecionado não existe
# e essa não é a melhor maneira de você fatiar até a parte final

print(frase[2:21:2])
# Agora ele está fazendo a mesma coisa do anterior, mas agora pulando
# de dois em dois

# Quando eu não coloco onde ele vai começar, ele começa do cactere 0
print(frase[:6])

print(frase[11:])
# Agora é o jeito certo de ir até o final sem ficar citando uma posição
# do array que nem existe

print(frase[11::3])
# Agora ele começa no 11, vai até o final e pula de 3 em 3

# Essa função faz mostrar quantas caracteres tem no array
print('Quantidade de caracteres: ',len(frase))

# Essa função conta quantas letras "a" tem na frase
print('Quantidade de letas "a":',frase.count('a'))

# Aqui ele vai contar quantas letras a tem entre a posição 0 e 5 do array
print('Quantidades de letras "a" entre 0 e 5:', frase.count('a',0,5))

# Ele procura e mostra onde começa a palavra "não"
print('Onde começa a palavra "não":', frase.find('não'))

# Se o find não achar a palavra ele retorna -1
print('Quantas vezes aparece a palavra "guaraná":', frase.find('guaraná'))

# Verifica se uma palavra está em uma frase
print('Existe a palavra "vaca" na frase:','vaca' in frase)

# Essa função é de transformação. Ele transformaa palavra "não" em um 
# espaço vazio. O replace não substitui na string, mas sim de uma forma
# secundária 
print(frase.replace('não',''))

# Essa função faz toda frase ficar em letras maiúscula
print(frase.upper())

# Essa função deixa todas as letras minúsculas
print(frase.lower())

# Essa função joga todas as letras para minúsculo e depois deixa só a 
# primeira maiúscula
print(frase.capitalize())

# Essa função joga todas as letras para minúsculo e depois deixa a primeira
# letra de todas as palavras em maiúsculo
print(frase.title())

frase2 = '   A Vaca Aprendeu a Nadar   ' 

print('\n', frase2)

# Essa função remove todos os espaços desnecessários no começo e no final
# da string
print(frase2.strip())

# Essa função só remove os últimos espaços desnecessários
print(frase2.rstrip())

# Essa função só remove os primeiros espaços desnecessários
print(frase2.lstrip())

# Essa função divide a string de acordo com cada palavra que tem, formando
# uma lista
lista_frase2 = frase2.split()
print(lista_frase2)

# Essa função coloca um "-" juntando a lista_frase2 que antes estava dividida
# e agora não está mais
print('-'.join(lista_frase2))

print("""\n\nEsse é um teste auto explicativo, basicamente em vez 
de você fazer vários prints você irá escrever um escrotamente fácil
dessa maneira e só ir apertando ENTER para ir para a próxima linha 
como um editor de texto normal.""")

# Essa função não só coloca todas as letras em maiúsculo 
print(frase2.upper().count('A'))