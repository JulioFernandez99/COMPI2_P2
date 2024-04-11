
from tabla.tablaSimbolos import Simbolos, TablaSimbolos

'''
    -Primero agrego un simbolo a la tabla local con el idDeclaracion y tipo "RFOROF"
    -Luego obtengo el simbolo con el idDeclarada 
    -Luego recorro el valor de la variable declarada y actualizo la variable declaracion con el valor actual
    -Luego proceso las instrucciones con la tabla local

'''

def procesar_for_of(instr, ts):
    from procesos.procesar_instrucciones import procesar_instrucciones
    TablaLocal = TablaSimbolos(ts.simbolos.copy()) 
    
    declarada=ts.obtener(instr.idDeclarada)
    
    TablaLocal.agregar(Simbolos(instr.idDeclaracion,"RFOROF",None))
    
    for valor in declarada.valor:
        TablaLocal.actualizar(instr.idDeclaracion,valor)
        brk=procesar_instrucciones(instr.instrucciones, TablaLocal)
        
        if brk:
            break
        elif brk=="TC":
            continue
    
    ts.salida+=TablaLocal.salida
    ts.errores+=TablaLocal.errores