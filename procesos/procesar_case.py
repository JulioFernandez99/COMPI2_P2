
from procesos.resolver_expresion import resolver_expresion
from tabla.tablaSimbolos import TablaSimbolos



def procesar_case(instr, ts,expLogSwitch):
    from procesos.procesar_instrucciones import procesar_instrucciones
    # expLogCase=None
    # TablaLocal = None
    #ts.salida+=expLogSwitch 
    cont=1
    default=None
    for caso in instr.casos:


        expLogCase=resolver_expresion(caso.expLogica,ts)
        if expLogCase==None:
            ts.salida+=f'''j default_case\n'''
            default=cont

            continue
        
        ts.salida+=f'''beq {expLogSwitch}, {expLogCase},case{cont}\n\n'''

        cont+=1

    cont=1
  
    end_switch=ts.get_break()
    for caso in instr.casos:
        if default==cont:
            ts.salida+=f'''default_case:\n'''
            procesar_instrucciones(caso.instrucciones, ts)
            cont+=1
            continue
        ts.salida+=f'''case{cont}:\n'''
        procesar_instrucciones(caso.instrucciones, ts)
        cont+=1

    ts.salida+=f'''{end_switch}:\n'''

    
   
        
    
    # for caso in instr.casos:
    #     ts.salida+=caso
        # expLogCase=resolver_expresion(caso.expLogica,ts)

        # if expLogSwitch==expLogCase: #Verifica los cases
        #     TablaLocal = TablaSimbolos(ts.simbolos.copy())
        #     procesar_instrucciones(caso.instrucciones, TablaLocal)
        #     ts.salida+=TablaLocal.salida
        #     ts.errores+=TablaLocal.errores
        #     break
            
            
            
            
        # if  expLogCase==None: #Verifica el default
        #     TablaLocal = TablaSimbolos(ts.simbolos.copy())
        #     procesar_instrucciones(caso.instrucciones, TablaLocal) 
        #     ts.salida+=TablaLocal.salida
        #     ts.errores+=TablaLocal.errores
            
       