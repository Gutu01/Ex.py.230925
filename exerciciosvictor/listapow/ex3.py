nota = float(input('Digite sua nota: '))

if nota >= 0 and nota< 6:
    print('Reprovado')
elif nota >= 6 and nota <= 10:
    print('Aprovado!')
else: 
    print('Nota inválida!')