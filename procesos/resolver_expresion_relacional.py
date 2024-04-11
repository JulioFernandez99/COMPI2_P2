from expresiones.operaciones import OPERACION_RELACION
from procesos.resolver_expresion_aritmetica import resolver_expresion_aritmetica


def resolver_expresion_relacional(expLog, ts):
    exp1 = resolver_expresion_aritmetica(expLog.exp1, ts)
    exp2 = resolver_expresion_aritmetica(expLog.exp2, ts)

    if expLog.operador == OPERACION_RELACION.MAYORQUE :   return exp1 > exp2
    if expLog.operador == OPERACION_RELACION.MENORQUE :   return exp1 < exp2
    if expLog.operador == OPERACION_RELACION.MAYORIGUAL : return exp1 >= exp2
    if expLog.operador == OPERACION_RELACION.MENORIGUAL : return exp1 <= exp2
    if expLog.operador == OPERACION_RELACION.IGUALIGUAL : return exp1 == exp2
    if expLog.operador == OPERACION_RELACION.DIFERENTE :  return exp1 != exp2
    
   