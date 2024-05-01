



def procesar_llamada_funcion(instr, ts):
    from procesos.procesar_funcion import procesar_funcion
    ts.salida+="-------------------"
    #ts.salida += f"jal----------- {instr.id}\n"
    # exp = procesar_funcion(instr, ts)
    # if(isinstance(exp,tuple)):
    #     return exp[0]
    # else:
    #     return exp