from app.funcoes import email_valido, dividir

def test_email_valido():
    assert email_valido("adcorrea@exem.com") is True
    assert email_valido("exemplo.com") is False


def test_dividir():
    assert dividir(1,1) == 1
    assert dividir(1,0) is None