print('Digite o seu período')
print('1-Matutino')
print('2-Vespertino')
print('3-Noturno')
turno = int(input('Resposta: '))

if turno == 1:
    print('Bom dia!')
elif turno == 2:
    print('Boa tarde!')
elif turno == 3:
    print('Boa noite!')
else:
    print('Valor inválido!')