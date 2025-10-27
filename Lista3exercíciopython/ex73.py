jose = 0
joao = 0
jacinto = 0
jeovana = 0
nulo = 0
branco = 0

print('Digite para votar')
print('1 - Jose')
print('2 - João')
print('3 - Jacinto')
print('4 - Jeovana')
print('5 - Voto Nulo')
print('6 - Voto em Branco')
print('0 - Finalizar')
resposta = int(input('Resposta: ')) 

while resposta != 0:
    if resposta == 1:
        jose = jose+1
    elif resposta == 2:
        joao = joao+1
    elif resposta == 3:
        jacinto = jacinto+1
    elif resposta == 4:
        jeovana = jeovana+1
    elif resposta == 5:
        nulo = nulo+1
    elif resposta == 6:
        branco = branco+1
    elif resposta == 0:
        print('O programa vai ser encerrado\n')
    else:
        print('\nCandidato não encontado')

    total_votos = jose+joao+jacinto+jeovana+nulo+branco

    print(f'\nTotal de votos para Jose: {jose}')
    print(f'Total de votos para João: {joao}')
    print(f'Total de votos para Jacinto: {jacinto}')
    print(f'Total de votos para Jeovana: {jeovana}')
    print(f'Total de votos nulos: {nulo}')
    print(f'Total de votos em branco: {branco}\n')
    print(f'Percentual de votos nulos %{nulo*100/total_votos:.2f}')
    print(f'Percentual de votos em branco %{branco*100/total_votos:.2f}')

    print('Digite para votar')
    print('1 - Jose')
    print('2 - João')
    print('3 - Jacinto')
    print('4 - Jeovana')
    print('5 - Voto Nulo')
    print('6 - Voto em Branco')
    print('0 - Finalizar')
    resposta = int(input('Resposta: ')) 