def palavras():

    palavras = []

    quantidade = int(input('Digite a quantidade de palavras a serem digitadas: '))

    for i in range(quantidade):
        palavras.append(input(f'Digite a {i+1}º palavra: '))

    relatorio(palavras)
    return palavras

def relatorio(palavras):

    maior_palavra = ''
    menor_palavra = ''
    vogais = 'AEIOU'
    a = 0

    comeca_vogal = []

    for i in palavras:

        if a == 0:
            maior_palavra = i
            menor_palavra = i
        else:
            if len(i) > len(maior_palavra):
                maior_palavra = i
            elif len(i) < len(menor_palavra):
                menor_palavra = i

        if i[0].upper() in vogais:
            comeca_vogal.append(i)
        a += 1
     
    print(f'\nVocê digitou {len(palavras)} palavras, vamos analisá-las:')
    print(f'Palavras que começam com vogais: {comeca_vogal}')
    print(f'Maior palavra: {maior_palavra}')
    print(f'Menor palavra: {menor_palavra}')

def Main():

    palavras()
    

Main()