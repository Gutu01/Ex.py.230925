while True:
    try:
        n = int(input('Digite um número inteiro: '))
        if n <= 0:
            print('Número inválido\nTente novamente!')
        else:
            break
    except ValueError:
        print('Número inválido!')
        

m = [1]
m_ = 1

while True:
    if sum(m) == n:
        print('Seu número é um quadrado perfeito!')
        break
    elif sum(m) > n:
        print('Seu número não um quadrado perfeito! :(')
        break
    
    m_ +=2
    m.append(m_)