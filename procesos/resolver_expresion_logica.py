from expresiones.operaciones import OPERACION_LOGICA
from procesos.resolver_expresion_aritmetica import resolver_expresion_aritmetica


def resolver_expresion_logica(instr, ts):
    from procesos.resolver_expresion import resolver_expresion
    operador=instr.operador
    
    if instr.operador==OPERACION_LOGICA.AND:
        exp1=resolver_expresion(instr.exp1,ts)
        exp2=resolver_expresion(instr.exp2,ts)
        
        return exp1 and exp2
    elif instr.operador==OPERACION_LOGICA.OR:
        exp1=resolver_expresion(instr.exp1,ts)
        exp2=resolver_expresion(instr.exp2,ts)
        return exp1 or exp2
    
        #print("instr.exp2",vars(instr.exp2))
    elif instr.operador==OPERACION_LOGICA.NOT:
        exp1=resolver_expresion(instr.exp1,ts)
        return not exp1
   