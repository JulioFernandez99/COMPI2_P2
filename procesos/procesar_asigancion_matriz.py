




from tabla.tablaSimbolos import TIPO_DATO


def procesar_asignacion_posicion_matriz(instr, ts):
    from procesos.resolver_expresion import resolver_expresion
    
    
    id = instr.id
    posiciones=instr.posiciones
    matriz=ts.obtener(id).valor
    exp=resolver_expresion(instr.exp, ts)

    # print("id",id)
    # print("posiciones",posiciones)
    # print("exp",exp)
    # print("matriz",matriz)

    indices = []
    for posicion in posiciones:
        indices.append(resolver_expresion(posicion, ts))

    acceder_posicion(matriz, indices, exp,ts)


    
def acceder_posicion(matriz, indices, nuevo_valor,ts):
    # Verificar si la matriz es válida y si los índices no están vacíos
    if not matriz or not indices:
        return None

    # Función recursiva para acceder a la posición en la matriz
    def _acceder(matriz, indices, nuevo_valor):
        if len(indices) == 1:  # Si solo queda un índice
            try:
                if 0 <= indices[0] < len(matriz):
                    matriz[indices[0]] = nuevo_valor
                    return matriz
                else:
                    return None
            except:
                print("Error: indice fuera de rango")
                ts.errores+="Error: indice fuera de rango\n"
        else:  # Si quedan más de un índice
            fila_actual = indices[0]

            try:
                if 0 <= fila_actual < len(matriz):
                    submatriz_modificada = _acceder(matriz[fila_actual], indices[1:], nuevo_valor)
                    if submatriz_modificada is not None:
                        matriz[fila_actual] = submatriz_modificada
                        return matriz
                    else:
                        return None
                else:
                    return None
            except:
                print("Error: indice fuera de rango")
                ts.errores+="Error: indice fuera de rango\n"

    return _acceder(matriz, indices, nuevo_valor)



    
  