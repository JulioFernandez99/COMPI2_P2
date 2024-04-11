from procesos.resolver_expresion import resolver_expresion
from tabla.tablaSimbolos import TablaSimbolos

def procesar_while(instr, ts):
    from procesos.procesar_instrucciones import procesar_instrucciones

    expLog = resolver_expresion(instr.expLogica, ts)
    
    existBreak=False
    
    while expLog and existBreak==False:
        TablaLocal = TablaSimbolos(ts.simbolos.copy())
        brk=procesar_instrucciones(instr.instrucciones,TablaLocal)
        
        #print("break",TablaLocal.existBreak)
        existBreak=TablaLocal.existBreak
        
        
        ts.salida+=TablaLocal.salida
        expLog = resolver_expresion(instr.expLogica, ts)

       
        
        