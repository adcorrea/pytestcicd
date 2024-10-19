import pytest
import time

def soma(a, b):
    return a + b

def multiplica(a, b):
    return a * b

@pytest.mark.lento
def test_soma_lenta():
    time.sleep(2)
    assert soma(1,1) == 2


@pytest.mark.rapido
def test_soma_rapida():
    assert soma(1,2) == 3



@pytest.mark.lento
def test_multiplica_lenta():
    time.sleep(2)
    assert multiplica(1,1) == 1
