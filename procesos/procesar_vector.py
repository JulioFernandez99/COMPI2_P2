


def procesar_vector(inst,ts):
    from procesos.resolver_expresion import resolver_expresion
    vector = []
    
    if len(inst.vector)==0:
        return []
    
    for exp in inst.vector:
        vector.append(resolver_expresion(exp,ts))
         
    return vector
    