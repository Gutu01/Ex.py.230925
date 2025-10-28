nome = input('Digite seu nome: ')

print('Digite seu sexo')
print('1-Masculino')
print('2-Feminino')
sexo = int(input('Resposta: '))

print('Digite seu estado civil')
print('1-Casado')
print('2-Solteiro')
print('3-Viúva')
print('4-Separado')
resposta = int(input('Resposta: '))

if sexo == 2 and resposta == 1:
    anos_casado = int(input('Digite quantos anos de casamento:'))