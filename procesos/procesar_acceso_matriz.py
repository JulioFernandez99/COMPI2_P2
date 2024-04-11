

def procesar_acceso_matriz(instr, ts):
    from procesos.resolver_expresion import resolver_expresion
    #print("procesar_acceso_matriz--------------------------------------")

    id=instr.id
    accesos=instr.accesos
    matriz=ts.obtener(id).valor
    tamMatriz=len(matriz)

    

    # print("id",id)
    # print("accesos",accesos)
    # print("matriz",matriz)
    # print("tamMatriz",tamMatriz)

    for acceso in accesos:
        valor=resolver_expresion(acceso,ts)
        
        if valor<0 or valor>=tamMatriz:
            print("Error: indice fuera de rango")
            ts.errores+="Error: indice fuera de rango\n"
            return "ERARA91"
        else:
            #print("valor",valor)
            matriz=matriz[valor]
            try:
                tamMatriz=len(matriz)
            except:
                pass
           

    return matriz


    
        
    