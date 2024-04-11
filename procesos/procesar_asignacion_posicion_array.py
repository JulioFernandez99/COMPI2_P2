




from tabla.tablaSimbolos import TIPO_DATO


def procesar_asignacion_posicion_array(instr, ts):
    from procesos.resolver_expresion import resolver_expresion
    id = instr.id
    exp = resolver_expresion(instr.exp, ts)
    posicion = resolver_expresion(instr.posicion, ts)
    
    vls = ts.obtener(id)
    #verificar que vls no sea constante
    if vls.constante == False:
        if vls.tipo == TIPO_DATO.ARRAY and type(exp) == int and type(posicion) == int:
            if posicion < len(vls.valor):
                vls.valor[posicion] = exp
                ts.actualizar(id, vls.valor)
            else:
                print("Error: posición no válida [",posicion,"]")
                ts.errores+="Error: posición no válida ["+str(posicion)+"]\n"
        else:
            print("Error: tipo de dato no válido")
            ts.errores+="Error: tipo de dato no válido\n"
    else:
        print("Error: No se puede modificar el valor de una constante")
        ts.errores+="Error: No se puede modificar el valor de una constante\n"