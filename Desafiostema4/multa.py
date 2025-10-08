velocidade = float(input('Digite a velocidade de um carro: '))
                 
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Você foi multado em R${multa:.2f}")
else:
    print('Você não foi multado!')