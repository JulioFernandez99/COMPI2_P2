

def procesar_retorno(instr, ts):
    from procesos.resolver_expresion import resolver_expresion

    return resolver_expresion(instr.exp, ts)