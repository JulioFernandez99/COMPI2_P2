from procesos.procesar_case import procesar_case
from procesos.resolver_expresion import resolver_expresion
from tabla.tablaSimbolos import TablaSimbolos

def procesar_switch(instr, ts):
    
    expLogSwitch = resolver_expresion(instr.expLogica, ts)
    procesar_case(instr, ts, expLogSwitch)