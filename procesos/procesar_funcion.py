






from instrucciones.instrucciones import Asignacion, Declaracion, ReturnInstr
from procesos.procesar_asignacion import procesar_asignacion
from procesos.procesar_declaracion import procesar_declaracion

from tabla.tablaSimbolos import TIPO_DATO, Simbolos, TablaSimbolos


def procesar_funcion(instr, ts):
    from procesos.resolver_expresion import resolver_expresion
    from procesos.procesar_instrucciones import procesar_instrucciones
    

    ts.salida += f"jal ra,{instr.id}\n"
    
    
    # paramesRecive = instr.parametros   
    # fun_ = ts.obtener(instr.id)
    # instrucciones = fun_.instrucciones
    # parametros = fun_.parametros
    # tipoRetorno = fun_.tipoRetorno
    
    # # print("parametros",parametros)
    # # print("paramesRecive",paramesRecive)
    # # print("instrucciones",instrucciones)
    
    
    # TablaLocal = TablaSimbolos(ts.simbolos.copy())
    
    # if len(parametros) == len(paramesRecive):
    #     for i in range(len(paramesRecive)):
    #         val=resolver_expresion(paramesRecive[i], ts)
    #         simbolo = Simbolos(parametros[i].id, parametros[i].tipo,val)
    #         TablaLocal.agregar(simbolo)
            
    # else:
    #     print("Error: la cantidad de parametros no coincide")
    #     ts.errores+="Error: la cantidad de parametros no coincide\n"
    #     return
        

    # try:
    #     instr, tipo_instr = procesar_instrucciones(instrucciones, TablaLocal)
    #     if isinstance(tipo_instr, ReturnInstr):
    #         ts.salida+=TablaLocal.salida
    #         ts.errores+=TablaLocal.errores
            

    #         #print("retorno...",tipoRetorno)

    #         #print("tipo retorno",instr)

    #         if isinstance(instr,int) and tipoRetorno == "number":
    #             return instr, tipo_instr
    #         elif isinstance(instr,float) and tipoRetorno == "float":
    #             return instr, tipo_instr
    #         elif isinstance(instr,str) and tipoRetorno == "string":
    #             return instr, tipo_instr
    #         elif isinstance(instr,bool) and tipoRetorno == "boolean":
    #             return instr, tipo_instr
    #         elif isinstance(instr,str) and tipoRetorno == "char" and len(instr)==1:
    #             return instr, tipo_instr
    #         else:
    #             print("Error: tipo de retorno no coincide")
    #             ts.errores+="Error: tipo de retorno no coincide\n"
    #             return None, None

            
    # except:
        
    #     ts.salida+=TablaLocal.salida
    #     ts.errores+=TablaLocal.errores
        

    

       
    
        

       