

from tabla.tablaSimbolos import Simbolos


def procesar_llamada_funcion_nativa_sin_paramtros(instr, ts) :
    from procesos.resolver_expresion import resolver_expresion
    
    
    funcion = instr.funcion
    
    if funcion=='pop':
        id = instr.id.id
        simbolo = ts.obtener(id)
        array = simbolo.valor
        if len(array)>0:
            eliminado=array.pop()
            ts.actualizar(id, array)
            return eliminado
        else:
            print('Error: El array esta vacio')
            ts.errores+='Error: El array esta vacio\n'
            
    elif funcion=='join':
        id = instr.id.id
        simbolo = ts.obtener(id)
        array = simbolo.valor
        return ','.join(map(str, array))   
            
    elif funcion=='length':
        id = instr.id.id
        simbolo = ts.obtener(id)
        array = simbolo.valor
        return len(array)
    
    elif funcion.lower()=='tostring':
        try:
            id = instr.id.id
            simbolo = ts.obtener(id)
            val = simbolo.valor
            return str(val)
        except:
            id = resolver_expresion(instr.id, ts)
            return str(id)
        
    elif funcion.lower()=='tolowercase':
        try:
            id = instr.id.id
            simbolo = ts.obtener(id)
            val = simbolo.valor
            return str(val).lower()
        except:
            id = resolver_expresion(instr.id, ts)
            return str(id).lower()
    
    elif funcion.lower()=='touppercase':
        try:
            id = instr.id.id
            simbolo = ts.obtener(id)
            val = simbolo.valor
            return str(val).upper()
        except:
            id = resolver_expresion(instr.id, ts)
            return str(id).upper()
            
        
            
            
        
   