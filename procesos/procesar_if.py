from procesos.resolver_expresion import resolver_expresion
from procesos.resolver_expresion_relacional import resolver_expresion_relacional
from tabla.tablaSimbolos import TablaSimbolos


def procesar_if(instr, ts):
    from procesos.procesar_instrucciones import procesar_instrucciones
    expLog = resolver_expresion_relacional(instr.expLogica, ts)
    salida = f'L{ts.generateLabel()}'
    ts.salida += f'j {salida}\n'

    #Instrucciones del if
    
    ts.salida += f'{expLog}:\n'
    procesar_instrucciones(instr.instrucciones,ts)


    ts.salida += f'{salida}:\n'