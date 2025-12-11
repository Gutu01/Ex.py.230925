

def notas():
    quantidade = int(input('Digite a quantidade: '))
    
    notas = []

    for i in range(quantidade):
        notas.append(float(input(f'Digite a {i+1}º nota: ')))

    return notas

def media(note):
    media = sum(note)/len(note)

    return media

def aprovacao(medi):

    if medi >= 6:
        aprovado = "Aprovado"
    elif medi >= 4 and medi <6:
        aprovado = "Recuperação"
    else:
        aprovado = "Reprovado"
    
    return aprovado

def Main():

    note = notas() 
    medi = media(note)
    aprovac = aprovacao(medi)

    print(note)
    print(medi)
    print(aprovac)

Main()