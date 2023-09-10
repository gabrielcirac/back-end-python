import pytest
from poesias.test_collection import PoesiaDB


@pytest.fixture
def db():
    return PoesiaDB()


def test_adicionar_e_obter_poesia(db):
    db.adicionar("O Mar", "Mar vasto, mar sem fim.")
    assert db.obter("O Mar") == "Mar vasto, mar sem fim."


def test_obter_poesia_inexistente(db):
    assert db.obter("Poesia Inexistente") is None
