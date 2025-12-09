peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura (em centimetros): '))

imc = peso/(altura*2)

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc <= 24.9:
    print('Você está com o peso ideal/adequado')
elif imc >= 25 and imc <= 29.9:
    print('Você está com sobrepeso')
else: 
    print('Você é considerado obeso')