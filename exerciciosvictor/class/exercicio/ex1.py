from classes import Pessoa

nome1 = input('Digite o nome da primeira pessoa: ')
idade1 = int(input('Digite o idade da primeira pessoa: '))
nome2 = input('Digite o nome da segunda pessoa: ')
idade2 = int(input('Digite a idade da segunda pessoa: '))

pessoa1 = Pessoa(nome1,idade1)
pessoa2 = Pessoa(nome2,idade2)

pessoa1.apresentar()
pessoa2.apresentar()