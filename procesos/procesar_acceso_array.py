

def procesar_acceso_array(instr, ts):
    from procesos.resolver_expresion import resolver_expresion
    id=instr.id
    acceso=resolver_expresion(instr.acceso, ts)
    
    data=ts.obtener(id)
    array=data.valor
    arraysize=len(array)
    
    if acceso>=0 and acceso<arraysize:
        return array[acceso]
    else:
        print("Error: indice fuera de rango")
        ts.errores+="Error: indice fuera de rango\n"
        return "ERARA91"
        
    