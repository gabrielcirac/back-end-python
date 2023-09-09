import pytest


def eh_palindromo(s):
    return s == s[::-1]


@pytest.mark.parametrize("input,expected", [
    ("radar", True),
    ("refer", True),
    ("python", False),
    ("", True),  # string vazia é considerada um palíndromo
])
def test_eh_palindromo(input, expected):
    assert eh_palindromo(input) == expected


# arquivo: test_fatorial.py


def fatorial(n):
    if n < 0:
        raise ValueError("Input deve ser um número não-negativo")
    elif n == 0 or n == 1:
        return 1
    else:
        fat = 1
        for i in range(2, n + 1):
            fat *= i
        return fat


@pytest.mark.parametrize("input,expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
])
def test_fatorial(input, expected):
    assert fatorial(input) == expected

# Testando a exceção


def test_fatorial_negative():
    with pytest.raises(ValueError) as exc_info:
        fatorial(-1)
    assert str(exc_info.value) == "Input deve ser um número não-negativo"
