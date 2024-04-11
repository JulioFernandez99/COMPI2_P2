
from procesos.resolver_expresion import resolver_expresion


def procesar_return(instr, ts):
    return resolver_expresion(instr.exp, ts)