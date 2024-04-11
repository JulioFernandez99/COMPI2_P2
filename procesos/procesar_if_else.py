


from procesos.resolver_expresion import resolver_expresion
from tabla.tablaSimbolos import TablaSimbolos


def procesar_if_else(instr, ts):
    from procesos.procesar_instrucciones import procesar_instrucciones
    expLog = resolver_expresion(instr.expLogica, ts)
    if expLog:
        TablaLocal = TablaSimbolos(ts.simbolos.copy())
        procesar_instrucciones(instr.instrIfVerdadero,TablaLocal)
        ts.salida+=TablaLocal.salida
        ts.errores+=TablaLocal.errores
        ts.existBreak=TablaLocal.existBreak
        ts.existContinue=TablaLocal.existContinue
    else:
        TablaLocal = TablaSimbolos(ts.simbolos.copy())
        procesar_instrucciones(instr.instrIfFalso,TablaLocal)
        ts.salida+=TablaLocal.salida
        ts.errores+=TablaLocal.errores
        ts.existBreak=TablaLocal.existBreak
        ts.existContinue=TablaLocal.existContinue
    
        
        