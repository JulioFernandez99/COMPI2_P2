
def guardar_interface(instr, ts):
    from procesos.resolver_expresion import resolver_expresion
    from tabla.tablaSimbolos import TIPO_DATO, Simbolos
    
    interface_id = instr.id
   
    props = instr.props
   
    
    keys = list(props.keys())
    values = list(props.values())
    #print("values",values)
    
   

    for i in range(len(keys)):
        instr.props[keys[i]] = values[i]
        
    
    simbolo = Simbolos(interface_id, TIPO_DATO.FUNCION, valor=None, props=instr.props)
    ts.agregar(simbolo)
    