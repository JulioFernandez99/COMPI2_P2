from tabla.tablaSimbolos import TIPO_DATO, Simbolos


def guardar_funcion(instr, ts):
    from procesos.procesar_instrucciones import procesar_instrucciones
    
    
    
    funcion_id = instr.id
    ts.salida += f"{funcion_id}:\n"
    procesar_instrucciones(instr.instrucciones, ts)
    ts.salida += f"ret\n"
    ts.funciones += ts.salida
    ts.salida = ""
    


    
    #print("parametros***********",instr.parametros  )
    
    # simbolo = Simbolos(funcion_id, TIPO_DATO.FUNCION,None, instrucciones=instr.instrucciones, parametros=instr.parametros,tipoRetorno=instr.retorno)
    # ts.agregar(simbolo)