import pytest
from app.classifica_idade import classifica_idade


@pytest.mark.crianca
@pytest.mark.parametrize('idade, faixa',
                         [(1,'Criança'), (11, 'Criança')])
def test_crianca(idade, faixa):
    assert classifica_idade(idade) == faixa



@pytest.mark.adulto
@pytest.mark.parametrize('idade, faixa',
                         [(18,'Adulto'), (59, 'Adulto')])
def test_adulto(idade, faixa):
    assert classifica_idade(idade) == faixa


@pytest.mark.adolescente
@pytest.mark.parametrize('idade, faixa',
                         [(12,'Adolescente'), (17, 'Adolescente')])
def test_adolescente(idade, faixa):
    assert classifica_idade(idade) == faixa


@pytest.mark.idoso
@pytest.mark.parametrize('idade, faixa',
                         [(60,'Idoso')])
def test_idoso(idade, faixa):
    assert classifica_idade(idade) == faixa