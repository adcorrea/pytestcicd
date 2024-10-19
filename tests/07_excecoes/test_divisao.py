import pytest
from app.funcoes import dividir_f


def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        dividir_f(1,0)


def test_dividir_por_zero2():
    with pytest.raises(ZeroDivisionError) as exec_info:
        dividir_f(1,0)

    assert 'Não é possível dividir por zero' in str(exec_info)