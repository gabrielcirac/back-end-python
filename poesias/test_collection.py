def somar(x, y):
    """Esta função soma dois números."""
    return x + y


class Poesia:
    def __init__(self, titulo, autor, versos):
        self.titulo = titulo
        self.autor = autor
        self.versos = versos

    def num_versos(self):
        return len(self.versos)

    def recitar(self, verso_num):
        try:
            return self.versos[verso_num]
        except IndexError:
            return "Verso não encontrado"


class PoesiaDB:
    def __init__(self):
        self._db = {}

    def adicionar(self, titulo, poesia):
        self._db[titulo] = poesia

    def obter(self, titulo):
        return self._db.get(titulo)
