from procesos.procesar_case import procesar_case
from procesos.resolver_expresion import resolver_expresion
from procesos.resolver_expresion_aritmetica import resolver_expresion_aritmetica
from tabla.tablaSimbolos import TablaSimbolos

def procesar_switch(instr, ts):
    
    #print(vars(instr))
    #ts.salida+=f"esta llegando a switch{instr.expLogica}\n"
    expLogSwitch = resolver_expresion_aritmetica(instr.expLogica, ts)
    #print("---",expLogSwitch)

    ts.salida+=f''' 
        swtich:
    '''
    
    procesar_case(instr, ts, expLogSwitch)