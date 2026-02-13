class Animal:
    def __init__(self, nome, peso, raca):
        self.nome = nome
        self.peso = peso
        self.raca = raca
    
    def nadar(self):
        print(f'\n{self.nome} com {self.peso} kg da raça {self.raca} está nadando')

    def voar(self):
        print(f'\n{self.nome} com {self.peso} kg da raça {self.raca} está voando')

    def pular(self):
        print(f'\n{self.nome} com {self.peso} kg da raça {self.raca} está pulando')