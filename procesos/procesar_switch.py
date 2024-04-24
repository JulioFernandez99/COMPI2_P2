from procesos.procesar_case import procesar_case
from procesos.resolver_expresion import resolver_expresion
from tabla.tablaSimbolos import TablaSimbolos

def procesar_switch(instr, ts):
    
    #print(vars(instr))
    expLogSwitch = resolver_expresion(instr.expLogica, ts)
    print("---",expLogSwitch)

    ts.salida+=f''' 
        swtich:
    '''
    procesar_case(instr, ts, expLogSwitch)