from procesos.resolver_expresion import resolver_expresion
from tabla.tablaSimbolos import TablaSimbolos


def procesar_if(instr, ts):
    from procesos.procesar_instrucciones import procesar_instrucciones
    
    expLog = resolver_expresion(instr.expLogica, ts)
    
    if expLog:
        TablaLocal = TablaSimbolos(ts.simbolos.copy()) 
        procesar_instrucciones(instr.instrucciones,TablaLocal)
        
        
        ts.existBreak=TablaLocal.existBreak
        ts.existContinue=TablaLocal.existContinue
        ts.salida+=TablaLocal.salida
            
    