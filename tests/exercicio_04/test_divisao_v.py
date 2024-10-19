import pytest
from app.funcoes import dividir_v


def test_divisio_by_zero():
    with pytest.raises(ValueError) as exec_info:
        dividir_v(1,0)

    assert 'O divisor não pode ser zero.' in str(exec_info)