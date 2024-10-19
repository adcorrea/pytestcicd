def email_valido (email):
    return "@" in email and "." in email

def dividir(a, b):
    if b == 0:
        return None
    
    return a/b


def dividir_f(a, b):
    if b == 0:
        raise ZeroDivisionError('Não é possível dividir por zero')
    
    return a/b


def dividir_v(a, b):
    if b == 0:
        raise ValueError("O divisor não pode ser zero.")
    return a / b