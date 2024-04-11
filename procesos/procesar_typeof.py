

def procesar_typeof(instr, ts):
    from procesos.resolver_expresion import resolver_expresion
    val=resolver_expresion(instr.exp, ts)
    if type(val).__name__=="int":
        return "number"
    elif type(val).__name__=="str":
        return "string"
    elif type(val).__name__=="list":
        return "array"
    elif type(val).__name__=="bool":
        return "boolean"
    
    
    