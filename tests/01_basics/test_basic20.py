def somar(a, b):
    return a + b


def comprimento(lista):
    return len(lista)


def test_somar_e_comprimento():
    assert somar(1, 2) == 3
    assert comprimento([1,3,3]) == 3