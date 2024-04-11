
from procesos.resolver_expresion import resolver_expresion
from tabla.tablaSimbolos import TablaSimbolos



def procesar_case(instr, ts,expLogSwitch):
    from procesos.procesar_instrucciones import procesar_instrucciones
    expLogCase=None
    TablaLocal = None
    
    
    
    for caso in instr.casos:
        expLogCase=resolver_expresion(caso.expLogica,ts)

        if expLogSwitch==expLogCase: #Verifica los cases
            TablaLocal = TablaSimbolos(ts.simbolos.copy())
            procesar_instrucciones(caso.instrucciones, TablaLocal)
            ts.salida+=TablaLocal.salida
            ts.errores+=TablaLocal.errores
            break
            
            
            
            
        if  expLogCase==None: #Verifica el default
            TablaLocal = TablaSimbolos(ts.simbolos.copy())
            procesar_instrucciones(caso.instrucciones, TablaLocal) 
            ts.salida+=TablaLocal.salida
            ts.errores+=TablaLocal.errores
            
       