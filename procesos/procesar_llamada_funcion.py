



def procesar_llamada_funcion(instr, ts):
    from procesos.procesar_funcion import procesar_funcion
    exp = procesar_funcion(instr, ts)
    if(isinstance(exp,tuple)):
        return exp[0]
    else:
        return exp