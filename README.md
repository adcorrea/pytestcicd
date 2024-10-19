COMANDOS PYTHON

Executa os testes
    python -m pytest

Abre o modo interativo do python
    python

Sai do modo interativo do python
    quit()


Executa teste com marcadores específicos
    python -m pytest -m lento
    python -m pytest -m "not lento"


executar cobertura de testes
    python pytest --cov=app.funcoes tests/08_plugins/test_basic3.py