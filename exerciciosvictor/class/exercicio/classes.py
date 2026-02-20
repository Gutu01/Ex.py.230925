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

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        return self.preco-self.preco*percentual/100
    
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura*self.altura