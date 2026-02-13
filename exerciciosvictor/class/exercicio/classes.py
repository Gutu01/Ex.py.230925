class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'\nOlá, eu sou {self.nome} e tenho {self.idade} anos.')

class ContaBancario:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, deposito):
        self.saldo += deposito

    def sacar(self, sacar):
        self.saldo -= sacar