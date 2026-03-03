from pessoa import Pessoa
from python import Python

while True:
    
    try:
        idade = int(input('Digite uma idade:'))
        break

    except ValueError:
        print('\nValor inválido!')
    
while True:
        
    try:
        notaEnem = int(input('Digite a nota do enem:'))
        break

    except ValueError:
        print('\nValor inválido!')
        

pessoa1 = Pessoa(idade, notaEnem)

while True:
    
    try:
        idade2 = int(input('Digite uma idade: '))
        break

    except ValueError:
        print('Valor inválido!')
        

python1 = Python(idade2, notaEnem)

print(pessoa1.calcular_idade(2026))
print(pessoa1.media_enem())

print(python1.calcular_idade(2026))
print(pessoa1.media_enem())



#   Existe também o except keyerror que mostra campo inexiste e o indexerror que mostra posição inválida