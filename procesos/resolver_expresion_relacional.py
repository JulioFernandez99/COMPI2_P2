from expresiones.operaciones import OPERACION_RELACION
from procesos.resolver_expresion_aritmetica import resolver_expresion_aritmetica


def resolver_expresion_relacional(expLog, ts):
    exp1 = resolver_expresion_aritmetica(expLog.exp1, ts)
    exp2 = resolver_expresion_aritmetica(expLog.exp2, ts)

    if expLog.operador == OPERACION_RELACION.MAYORQUE :   
        etiqueta = f'L{ts.generateLabel()}'
        ts.salida += f'bgt {exp1}, {exp2}, {etiqueta}\n'
        return etiqueta
    if expLog.operador == OPERACION_RELACION.MENORQUE :   
        etiqueta = f'L{ts.generateLabel()}'
        ts.salida += f'blt {exp1}, {exp2}, {etiqueta}\n'
        return etiqueta
    if expLog.operador == OPERACION_RELACION.MAYORIGUAL : 
        return exp1 >= exp2
    if expLog.operador == OPERACION_RELACION.MENORIGUAL : 
        etiqueta = f'L{ts.generateLabel()}'
        ts.salida += f'ble {exp1}, {exp2}, {etiqueta}\n'
        return etiqueta
    if expLog.operador == OPERACION_RELACION.IGUALIGUAL : 
        etiqueta = f'L{ts.generateLabel()}'
        ts.salida += f'beq {exp1}, {exp2}, {etiqueta}\n'
        return etiqueta
    if expLog.operador == OPERACION_RELACION.DIFERENTE :  
        etiqueta = f'L{ts.generateLabel()}'
        ts.salida += f'bne {exp1}, {exp2}, {etiqueta}\n'
        return etiqueta
    
   