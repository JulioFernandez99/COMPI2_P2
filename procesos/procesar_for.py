
from expresiones.operaciones import OPERACION_ARITMETICA
from procesos.procesar_declaracion import procesar_declaracion
from procesos.resolver_expresion import resolver_expresion
from tabla.tablaSimbolos import TIPO_DATO, TablaSimbolos


def procesar_for(instr, ts):
    from procesos.procesar_instrucciones import procesar_instrucciones
   
    
    ciclo=f"L{ts.generateLabel()}"
    
    end_for = ts.get_break()
    procesar_declaracion(instr.declaracion, ts)
    ts.salida += f"{ciclo}:\n"
    valExpLog = resolver_expresion(instr.expLogica, ts)
    ts.salida += f"j {end_for}\n"
    ts.salida += f"{valExpLog}:\n"
    procesar_instrucciones(instr.instrucciones, ts)
    
    actualizar(instr.actualizacion, ts)

    ts.salida += f"j {ciclo}\n"



    ts.salida += f"{end_for}:\n"
    ts.pop_break()


    
#     procesar_declaracion(instr.declaracion, TablaLocal) 
#     valExpLog=resolver_expresion(instr.expLogica, TablaLocal)
    
#     while valExpLog:
#         brk=procesar_instrucciones(instr.instrucciones, TablaLocal)
#         actualizar(instr.actualizacion, TablaLocal)
#         valExpLog=resolver_expresion(instr.expLogica, TablaLocal)    
    
    
#     ts.salida+=TablaLocal.salida
#     ts.errores+=TablaLocal.errores
    
def actualizar(instr, ts):
    if instr.operador == OPERACION_ARITMETICA.AUMENTO:
        temporal = ts.generateTemporal()
        temporal2 = ts.generateTemporal()
        ts.salida += f"la {temporal},{instr.id}\n"
        ts.salida += f"lw {temporal2},0({temporal})   \n"
        ts.salida += f"addi {temporal2},{temporal2},1\n"
        ts.salida += f"sw {temporal2},0({temporal})\n"
        ts.stack_push(temporal)
        ts.stack_push(temporal2)

    else:   
        temporal = ts.generateTemporal()
        temporal2 = ts.generateTemporal()
        ts.salida += f"la {temporal},{instr.id}\n"
        ts.salida += f"lw {temporal2},0({temporal})   \n"
        ts.salida +=f"addi {temporal2},{temporal2},-1\n"
        ts.salida += f"sw {temporal2},0({temporal})\n"
        ts.stack_push(temporal)
        ts.stack_push(temporal2)
    
    #ts.salida += f"{instr.operador}\n"
    

   