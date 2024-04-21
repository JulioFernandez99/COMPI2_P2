


from procesos.resolver_expresion import resolver_expresion
from procesos.resolver_expresion_relacional import resolver_expresion_relacional
from tabla.tablaSimbolos import TablaSimbolos


def procesar_if_elif_else(instr, ts):
    from procesos.procesar_instrucciones import procesar_instrucciones
    expLog = resolver_expresion_relacional(instr.expLogica, ts)
    salida = f'LSalida'
    siguiente = f'L{ts.generateLabel()}'
    ts.salida += f'j {siguiente}\n'

    # #Instrucciones del if
    
    ts.salida += f'{expLog}:\n'
    procesar_instrucciones(instr.instrIfVerdadero,ts)
    ts.salida += f'j {salida}\n'



    ts.salida += f'{siguiente}:\n'
        
    for data in instr.instrIfFalso:
        expLog = resolver_expresion_relacional(data.expLogica, ts)
        siguiente = f'L{ts.generateLabel()}'
        ts.salida += f'j {siguiente}\n'

    #     #Instrucciones del if
        
        ts.salida += f'{expLog}:\n'
        procesar_instrucciones(data.instrucciones,ts)
        ts.salida += f'j {salida}\n'
        ts.salida += f'{siguiente}:\n'

    procesar_instrucciones(instr.instrIfElse,ts)
    

    #     ts.salida += f'{caso_falso}:\n'
    #     procesar_instrucciones(instr.instrIfFalso,ts)

    #     ts.salida += f'{salida}:\n'


    ts.salida += f'{salida}:\n'