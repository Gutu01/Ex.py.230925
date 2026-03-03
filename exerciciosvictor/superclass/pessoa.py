class Pessoa:
    def __init__(self, anoNasc, notaEnem):
        self.anoNasc = anoNasc
        self.notaEnem = notaEnem

    def calcular_idade(self, ano) -> int:
        return int(ano - self.anoNasc)
    
    def media_enem(self):
        return self.notaEnem * 0.9