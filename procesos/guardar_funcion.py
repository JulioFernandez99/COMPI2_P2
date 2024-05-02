from procesos.procesar_declaracion import procesar_declaracion
from tabla.tablaSimbolos import TIPO_DATO, Simbolos


def guardar_funcion(instr, ts):
    from procesos.procesar_instrucciones import procesar_instrucciones
    
    arr=[]
    if len(instr.parametros) > 0:
        
        for param in instr.parametros:
            arr.append(param.id)
            if param.tipo == "string":
                ts.dato += f"{param.id}: .asciz \" \"\n"
            elif param.tipo == "number":
                ts.dato += f"{param.id}: .word 0\n"
            #ts.salida += f"...{vars(param)}:\n"

        ts.parametros[instr.id] = arr
        funcion_id = instr.id
        ts.salida += f"{funcion_id}:\n"
        procesar_instrucciones(instr.instrucciones, ts)
        ts.salida += f"ret\n"
        ts.funciones += ts.salida
        ts.salida = ""

    
    else:
        funcion_id = instr.id
        ts.salida += f"{funcion_id}:\n"
        procesar_instrucciones(instr.instrucciones, ts)
        ts.salida += f"ret\n"
        ts.funciones += ts.salida
        ts.salida = ""
    


    
    #print("parametros***********",instr.parametros  )
    
    # simbolo = Simbolos(funcion_id, TIPO_DATO.FUNCION,None, instrucciones=instr.instrucciones, parametros=instr.parametros,tipoRetorno=instr.retorno)
    # ts.agregar(simbolo)