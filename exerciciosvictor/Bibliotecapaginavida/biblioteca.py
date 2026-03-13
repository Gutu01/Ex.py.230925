class Biblioteca:
    def __init__(self, livro):
        self._livro = livro
        self._emprestado = False

    @property
    def get_emprestimo(self):
        return self._emprestado

    @get_emprestimo.setter
    def set_emprestimo(self):
        self._emprestado = True
        print('O livro foi emprestado!')

    @get_emprestimo.setter
    def set_devolucao(self):
        self._emprestado = False
        print('O liro foi devolvido!')