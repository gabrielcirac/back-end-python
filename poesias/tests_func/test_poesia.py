# test_poesia.py
import unittest


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


class TestPoesia(unittest.TestCase):

    def setUp(self):
        self.poema = Poesia("Soneto de Separação", "Vinícius de Moraes", [
            "De repente do riso fez-se o pranto",
            "Silencioso e branco como a bruma",
            "E das bocas unidas fez-se a espuma",
            "E das mãos espalmadas fez-se o espanto."
        ])

    def test_num_versos(self):
        self.assertEqual(self.poema.num_versos(), 4)

    def test_recitar(self):
        self.assertEqual(self.poema.recitar(
            1), "Silencioso e branco como a bruma")
        self.assertEqual(self.poema.recitar(4), "Verso não encontrado")


if __name__ == "__main__":
    unittest.main()
