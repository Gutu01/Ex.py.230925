dias = ["domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado"]

resposta = int(input('Escolha um dia da semana digitando um número de 0 à 6:'))

if resposta == 0 or resposta == 6:
    print(f'Você escolhe a {dias[resposta]} e não é um dia útil')
else:
    print(f'Você escolhe a {dias[resposta]} e é um dia útil')