

from tabla.tablaSimbolos import Simbolos


def procesar_llamada_funcion_nativa_con_paramtros(instr, ts) :
    from procesos.resolver_expresion import resolver_expresion
    
    
    funcion = instr.funcion

    if funcion=='indexOf':
        data=resolver_expresion(instr.id, ts)
        parametro=resolver_expresion(instr.parametro[0], ts)
        if isinstance(data, list):
            try:
                return data.index(parametro)
            except:
                print("Error:",parametro," no existe en el array")
                #ts.errores+="Error: "+str(parametro)+" no existe en el array\n"
                return -1
                #return "ERARA91"
            
    elif funcion=='push':
        data=resolver_expresion(instr.id, ts)
        parametro=resolver_expresion(instr.parametro[0], ts)
        if isinstance(data, list):
            data.append(parametro)
            return data
        
            
   