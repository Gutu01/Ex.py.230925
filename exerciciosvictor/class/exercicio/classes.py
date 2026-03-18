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
    
class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.__velocidade = 0
        #Aqui é um tentativa de deixar as variáveis privadas. Como eu disse, é uma tentativa, onde a velocidade está privada e modelo não pois a velocidade é um atributo que pode quebrar o código, segundo meu raciocínio. Não usei o @property pois em nenhum momento faço uma permissão de acesso externo controlado isoladamente (segundo o chatgpt).

    def acelerar(self):
        valor = float(input('\nDigite o valor da aceleração (km):'))
        self.__velocidade += valor
        print(f'\nA velocidade {self.modelo} atualmente é de Km {self.__velocidade}')

    def freiar(self):
        valor = float(input('\nDigite o valor do freio (km):'))
        if valor > self.__velocidade:
            print(f'O valor é maior do que a velocidade atual do {self.modelo}')
        else:
            self.__velocidade -= valor
            print(f'\nA velocidade {self.modelo} atualmente é de Km {self.__velocidade}')

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.__media = 0

    def media(self):
        self.__media = (self.nota1 + self.nota2)/2
        return f'\nA média de {self.nome} é de {self.__media}'
    
    def situacao(self):
        if self.__media >= 7:
            return f'{self.nome} foi aprovado!'
        else:
            return f'{self.nome} foi reprovado!'
        
class Lampada:
    def __init__(self):
        self.ligada = False 

    def ligar(self):
        self.ligada = True
    
    def desligar(self):
        self.ligada = False

    def estado(self):
        if self.ligada:
            print('Ligada')
        else:
            print('Desligada')

class Livro:
    def __init__(self):
        self.titulo = 'Sua mae'
        self.autor = 'Sua avó'
        self.quantidade = 3
        self.emprestado = 0

    def emprestar(self):
        if self.emprestado == self.quantidade:
            return False
        else:
            self.emprestado += 1
            return True
    
    def devolver(self):
        if self.emprestado == 0:
            return False
        else:
            self.emprestado -= 1
            return True
        

class Termometro:
    def __init__(self, celsius):
        self.celsius = celsius

    def para_fahrenheit(self):
        return f'{self.celsius}Cº = {self.celsius * 9/5 + 32}Fº'
    
    def para_kelvin(self):
        return f'{self.celsius}Cº = {self.celsius + 273.15}Kº'
    
class Televisao:
    def __init__(self):
        self.volume = 10
        self.canal = 1

    def aumentar_volume(self):
        self.volume += 1
    
    def diminuir_volume(self):
        self.volume -= 1

    def trocar_canal(self, numero):
        self.canal = numero

class Cronometro:
    def __init__(self):
        self.segundos = 0

    def tic(self):
        self.segundos += 1

    def avançar(self, n):
        self.segundos += n

    def zerar(self):
        self.segundos = 0

class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, nome, preco):
        self.itens.append([nome, preco])

    def total(self):
        soma = 0
        for i in self.itens:
            soma += i[1]
        print(f'O total da sua compra é de R${soma}')