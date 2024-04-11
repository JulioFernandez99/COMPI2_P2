



def procesar_asignacion_struct(instr,ts):
    from procesos.resolver_expresion import resolver_expresion
    #print("procesar_asignacion_struct---------------")
    #print("instr",vars(instr))
    id1=instr.id.id
    id2=instr.id2.id
    
    if instr.exp is not None:
        exp=resolver_expresion(instr.exp,ts)
        obj=ts.obtener(id1)
        
        props=obj.props
        
        #print("propssss",props[id2])
        
        if props[id2] == "number" and type(exp) is int:
            props[id2]=exp
        elif props[id2] == "string" and type(exp) is str:
            props[id2]=exp
        elif props[id2] == "boolean" and type(exp) is bool:
            props[id2]=exp
        elif props[id2] == "char" and type(exp) is str:
            props[id2]=exp
        else:
            print("Error: tipo de dato no válido",props[id2],type(exp))
            ts.errores+="Error: tipo de dato no válido\n"
            
        
        
        
        
    else:
        print("imprimir",id1,id2)
        return ts.obtener(id1).props[id2]
    
   
    
    # id=instr.id.id
    
    # obj=ts.obtener(instr.id.id)
    # props=obj.props
    # print("props",props)
    