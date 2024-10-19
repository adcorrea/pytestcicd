import pytest
from app.fatorial import fatorial

@pytest.mark.parametrize('numero, n_fatorial', [(0,1), (1, 1), (5, 120)])
def test_fatorial(numero, n_fatorial):
    assert fatorial(numero) == n_fatorial