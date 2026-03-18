from classes import Aluno

alunos = []

for i in range(3):
    nome = input('Digite seu nome: ')
    nota1 = float(input('Digite a primeira nota:'))
    nota2 = float(input('Digite a segunda nota:'))

    aluno = Aluno(nome,nota1,nota2)
    alunos.append(aluno)

for i in alunos:
    print(i.media())    
    print(i.situacao())    