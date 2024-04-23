#---------------------------------------ASIGNACIONES--------------------------------------
from expresiones.operaciones import OPERACION_ARITMETICA

from procesos.resolver_expresion import resolver_expresion

from tabla.tablaSimbolos import TIPO_DATO


def procesar_asignacion(instr, ts):
    
    id = instr.id
    exp = resolver_expresion(instr.exp, ts)
    vls = ts.obtener(id) 
    

    

    
    
    #zprint("llegue aca*-----------------",vls.tipo,exp,type(exp),instr.exp)
    
    if exp!="ERARA91":#este error es para cuando se intenta acceder a una posicion que no existe en el array
        
        if vls.tipo == TIPO_DATO.ENTERO and type(exp) == int and vls.constante == False:
            ts.actualizar(id, exp)
            
            lasttemporal = ts.lastTemporal()
            temporal = ts.generateTemporal()
            ts.salida += f'la {temporal}, {id}\n'
            ts.salida += f'sw {lasttemporal}, 0({ts.lastTemporal()})\n'
        elif vls.tipo == TIPO_DATO.DECIMAL and type(exp) == float and vls.constante == False:
            ts.actualizar(id, exp)
            lasttemporal = ts.lastTemporal()
            temporal = ts.generateTemporal()
            ts.salida += f'la {temporal}, {id}\n'
            ts.salida += f'sw {lasttemporal}, 0({ts.lastTemporal()})\n'
        elif vls.tipo == TIPO_DATO.BOOLEAN and type(exp) == bool and vls.constante == False:
            ts.actualizar(id, exp) 
            lasttemporal = ts.lastTemporal()
            temporal = ts.generateTemporal()
            ts.salida += f'la {temporal}, {id}\n'
            ts.salida += f'sw {lasttemporal}, 0({ts.lastTemporal()})\n'
        elif vls.tipo == TIPO_DATO.STRING and type(exp) == str and vls.constante == False:
            ts.actualizar(id, exp)
            lasttemporal = ts.lastTemporal()
            temporal = ts.generateTemporal()
            ts.salida += f'la {temporal}, {id}\n'
            ts.salida += f'sw {lasttemporal}, 0({ts.lastTemporal()})\n'
        elif vls.tipo == TIPO_DATO.CHAR and type(exp) == str and vls.constante == False:
            ts.actualizar(id, exp)
        elif vls.tipo == "RFOROF":
            print("Error: No se posible asignar valor a esta variable,pertenece a forOf")
            ts.errores+="Error: No se posible asignar valor a esta variable,pertenece a forOf\n"
     
        elif vls.constante == True:
            print("Error: No se puede modificar el valor de una constante")
            ts.errores+="Error: No se puede modificar el valor de una constante\n"
        else:
            print("Error: tipo de dato no válido***+",vls.tipo,exp,type(exp))
            ts.errores+="Error: tipo de dato no válido\n"

def procesar_asignacion_operador(instr, ts):
    
    id = instr.id
    exp = resolver_expresion(instr.exp, ts)
    vls = ts.obtener(id)
   
    if vls.tipo == TIPO_DATO.ENTERO and type(exp) == int:
        if instr.operador == OPERACION_ARITMETICA.MAS:
            ts.actualizar(id, int(vls.valor)+int(exp))
        elif instr.operador == OPERACION_ARITMETICA.MENOS:
            ts.actualizar(id, int(vls.valor)-int(exp))
        else:
            print("Error: tipo de dato no válido")
            ts.errores+="Error: tipo de dato no válido\n"
            
    elif vls.tipo == TIPO_DATO.DECIMAL and type(exp) == float:
        
        if instr.operador == OPERACION_ARITMETICA.MAS:
            ts.actualizar(id, float(vls.valor)+float(exp))
        elif instr.operador == OPERACION_ARITMETICA.MENOS:
            ts.actualizar(id, float(vls.valor)-float(exp))
        else:
            print("Error: tipo de dato no válido")
            ts.errores+="Error: tipo de dato no válido\n"
        
    elif vls.tipo == TIPO_DATO.STRING and type(exp) == str: 
        ts.actualizar(id, vls.valor+exp)
    elif vls.tipo == TIPO_DATO.CHAR and type(exp) == str:
        ts.actualizar(id, vls.valor+exp)
    else:
        print("Error: tipo de dato no válido")
        ts.errores+="Error: tipo de dato no válido\n"

   