from poesias.test_collection import somar, Poesia


def test_somar():
    """Teste para verificar se a função de soma está funcionando corretamente."""
    assert somar(1, 2) == 3
    assert somar(-1, -1) == -2
    assert somar(0, 0) == 0


def test_num_versos():
    poema = Poesia("Soneto de Separação", "Vinícius de Moraes", [
        "De repente do riso fez-se o pranto",
        "Silencioso e branco como a bruma",
        "E das bocas unidas fez-se a espuma",
        "E das mãos espalmadas fez-se o espanto."
    ])

    assert poema.num_versos() == 4


def test_recitar():
    poema = Poesia("Soneto de Separação", "Vinícius de Moraes", [
        "De repente do riso fez-se o pranto",
        "Silencioso e branco como a bruma",
        "E das bocas unidas fez-se a espuma",
        "E das mãos espalmadas fez-se o espanto."
    ])

    assert poema.recitar(1) == "Silencioso e branco como a bruma"
    assert poema.recitar(4) == "Verso não encontrado"

# Arquivo: test_simple_functions.py


def greet(name):
    return f"Hello, {name}"


def test_greet():
    assert greet("World") == "Hello, World"
    assert greet("") == "Hello, "
    assert greet(123) == "Hello, 123"
