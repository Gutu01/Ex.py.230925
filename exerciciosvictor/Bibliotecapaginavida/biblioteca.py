class Biblioteca:
    def __init__(self,nome):
        self._nome = nome
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f'{self._nome} foi emprestado com sucesso!')
        else:
            print(f'{self._nome} não está disponível para emprestimo!')
    
    def devolver(self):
        if self.disponivel:
            print(f'{self._nome} não foi emprestado!')
        else:
            self.disponivel = True
            print(f'{self._nome} foi devolvido com sucesso!')

    def status(self):
        if self.disponivel:
            print('O livro está disponível.')
        else:
            print('O livro está indisponível.')