import pytest

@pytest.fixture(scope="function")
def get_lista():
    lista = [1, 2, 3]
    return lista


def soma_dobro(numeros):  
    return sum(x * 2 for x in numeros)


def test_soma_dobro(get_lista):
    assert soma_dobro(get_lista) == 12