import pytest
from app.classifica_idade import classifica_idade


@pytest.mark.parametrize("idade, esperado", [
        (11, 'Criança'),(12, 'Adolescente'),
        (18, 'Adulto'), (60, 'Idoso')])
def test_classifica_idade(idade, esperado):
    assert classifica_idade(idade) == esperado