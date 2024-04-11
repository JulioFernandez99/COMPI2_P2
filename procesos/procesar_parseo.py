



def procesar_parseo(instr,ts):
    from procesos.resolver_expresion import resolver_expresion
    
    tipo=instr.tipo
    exp=resolver_expresion(instr.exp,ts)
    #print("TIPO----",tipo)
    
    
    if tipo=="parseInt":
        #print("EXPRESION----",exp)
        try:    
            return int(exp)
        except:
            
            return int(float(exp))
    
    elif tipo=="parseFloat":
        try:
            return float(exp)
        except:
            return float(int(exp))
    
    elif tipo=="toString":
        return str(exp)
    
    else:
        print("ERROR: tipo de parseo no reconocido")
        ts.errores+="ERROR: tipo de parseo no reconocido\n"
        return "ERARA91"
    
    
        
        
    # print("TIPO----",tipo)
    # print("EXPRESION----",exp)
    