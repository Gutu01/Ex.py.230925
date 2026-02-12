from pessoa import Pessoa

nome = input('Digite um nome: ')
idade = int(input('Digite uma idade: '))
sexo = input('Digite um sexo: ')

Pessoa1 = Pessoa(nome, idade, sexo)
Pessoa1.andar()