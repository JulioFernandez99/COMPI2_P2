
from expresiones.operaciones import OPERACION_ARITMETICA
from procesos.procesar_declaracion import procesar_declaracion
from procesos.resolver_expresion import resolver_expresion
from tabla.tablaSimbolos import TIPO_DATO, TablaSimbolos


def procesar_for(instr, ts):
    from procesos.procesar_instrucciones import procesar_instrucciones
    TablaLocal = TablaSimbolos(ts.simbolos.copy())
   
    
 
    
    procesar_declaracion(instr.declaracion, TablaLocal) 
    valExpLog=resolver_expresion(instr.expLogica, TablaLocal)
    
    while valExpLog:
        brk=procesar_instrucciones(instr.instrucciones, TablaLocal)
        actualizar(instr.actualizacion, TablaLocal)
        valExpLog=resolver_expresion(instr.expLogica, TablaLocal)    
    
    
    ts.salida+=TablaLocal.salida
    ts.errores+=TablaLocal.errores
    
    
def actualizar(instr, ts):
    valID=ts.obtener(instr.id)
    #print('valID antes:', valID.valor)
    valor=valID.valor
    #print("valor antes de actualizacion:",valor)
    if valID.tipo == TIPO_DATO.ENTERO:
        valor = int(valID.valor)
    elif valID.tipo == TIPO_DATO.DECIMAL:
        valor = float(valID.valor)
    elif valID.tipo == TIPO_DATO.STRING:
        valor = str(valID.valor)
    elif valID.tipo == TIPO_DATO.BOOLEAN:
        valor = bool(valID.valor)
    elif valID.tipo == TIPO_DATO.CHAR:
        valor = str(valID.valor)
    if instr.operador == OPERACION_ARITMETICA.AUMENTO:
        valor += 1
    elif instr.operador == OPERACION_ARITMETICA.DECREMENTO:
        valor -= 1
    
    ts.actualizar(instr.id, valor)
    
    #valID=ts.obtener(instr.id)
    #print('valID despues:', valID.valor)