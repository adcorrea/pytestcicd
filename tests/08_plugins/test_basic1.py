def is_positive(numero):
    return numero > 0


def test_positivo():
    assert is_positive(5) is True
    assert is_positive(-1) is False