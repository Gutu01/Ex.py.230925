import pessoa

class Python(pessoa.Pessoa):
    def __init__(self, anoNasc, notaEnem):
        super().__init__(anoNasc, notaEnem)

    def media_enem(self):
        return self.notaEnem * 0.8