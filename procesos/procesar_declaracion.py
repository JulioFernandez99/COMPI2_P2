#--------------------------------------DECLARACIONES-------------------------------------


import numpy as np
from tabla.tablaSimbolos import TIPO_DATO, Simbolos


def declaracion_con_tipo_sin_valor(tipoVariable, tipoDec, id, ts):
    #print("-------------------Declaracion con tipo y sin valor-------------------")
    #print("tipovariable", tipoVariable)
    #print("tipodeclaracion", tipoDec)
    
    from procesos.resolver_expresion import resolver_expresion
    if tipoVariable == "number":
        simbolo = Simbolos(id, TIPO_DATO.ENTERO, 0)
        ts.agregar(simbolo)
    elif tipoVariable == "float":
        simbolo = Simbolos(id, TIPO_DATO.DECIMAL, 0.0)
        ts.agregar(simbolo)
    elif tipoVariable == "boolean":
        simbolo = Simbolos(id, TIPO_DATO.BOOLEAN, True)
        ts.agregar(simbolo)
    elif tipoVariable == "string":
        simbolo = Simbolos(id, TIPO_DATO.STRING, "")
        ts.agregar(simbolo)
    elif tipoVariable == "char":
        simbolo = Simbolos(id, TIPO_DATO.CHAR, "")
        ts.agregar(simbolo)
    elif tipoVariable == "number[]":
        simbolo = Simbolos(id, TIPO_DATO.ARRAY, [])
        ts.agregar(simbolo)
    elif tipoVariable == "float[]":
        simbolo = Simbolos(id, TIPO_DATO.ARRAY, [])
        ts.agregar(simbolo)
    elif tipoVariable == "boolean[]":
        simbolo = Simbolos(id, TIPO_DATO.ARRAY, [])
        ts.agregar(simbolo)
    elif tipoVariable == "string[]":
        simbolo = Simbolos(id, TIPO_DATO.ARRAY, [])
        ts.agregar(simbolo)
    elif tipoVariable == "char[]":
        simbolo = Simbolos(id, TIPO_DATO.ARRAY, [])
        ts.agregar(simbolo)
    else:
        print("Error1: tipo de dato no válido")    
        ts.errores+="Error1: tipo de dato no válido\n"
        
def declaracion_const(exp,tipoVariable, tipoDec,tipoValor, id, ts):
    # print("-------------------Declaracion de una contante-------------------")
    # print("tipovariable", tipoVariable)
    # print("tipodeclaracion", tipoDec)
    # print("tipovalor", tipoValor)  
    
    # print("expresion resuelta------",exp,tipoDec,tipoVariable,tipoValor)
    
    if tipoVariable is None and tipoValor is type(None):
        print("Error: Las constantes deben de venir con un tipo de dato")
    else:
        if (tipoVariable == "number" or tipoVariable==None) and tipoValor is type(1):
            simbolo = Simbolos(id, TIPO_DATO.ENTERO, exp ,True)
            ts.agregar(simbolo)
            
        elif (tipoVariable == "number" or tipoVariable==None) and tipoValor is type(1.1):
            simbolo = Simbolos(id, TIPO_DATO.DECIMAL, exp ,True)
            ts.agregar(simbolo)
        elif (tipoVariable == "float"  or tipoVariable==None) and tipoValor is type(1.1):
            simbolo = Simbolos(id, TIPO_DATO.DECIMAL, exp,True)
            ts.agregar(simbolo)
        elif (tipoVariable == "float" or tipoVariable==None) and tipoValor is type(1):
            simbolo = Simbolos(id, TIPO_DATO.DECIMAL, float(exp),True)
            ts.agregar(simbolo)
        elif (tipoVariable == "boolean" or tipoVariable==None) and tipoValor is type(True):
            simbolo = Simbolos(id, TIPO_DATO.BOOLEAN, exp ,True)
            ts.agregar(simbolo)
        elif (tipoVariable == "string" or tipoVariable==None) and tipoValor is type(""):
            simbolo = Simbolos(id, TIPO_DATO.STRING, exp ,True)
            ts.agregar(simbolo)
        elif (tipoVariable == "char" or tipoVariable==None ) and tipoValor is type(""):
            simbolo = Simbolos(id, TIPO_DATO.CHAR, exp ,True)
            ts.agregar(simbolo)
        elif tipoValor is type([]):
            
            valida,rows=es_matriz(exp)
            #print("Valida",valida)
        # print("Rows",rows)

            if valida!=None:
                if valida:
                    simbolo = Simbolos(id, TIPO_DATO.MATRIZ, exp)
                    ts.agregar(simbolo)
                else:
                    simbolo = Simbolos(id, TIPO_DATO.ARRAY, exp)
                    ts.agregar(simbolo)

            
            else:
                simbolo = Simbolos(id, TIPO_DATO.ARRAY, exp)
                ts.agregar(simbolo)


            # simbolo = Simbolos(id, TIPO_DATO.ARRAY, exp ,True)
            # ts.agregar(simbolo)
        else:
            print("Error2: tipo de dato no válido",tipoValor,tipoVariable)
            ts.errores+="Error2: tipo de dato no válido\n"
        
def declaracion_con_tipo_con_valor(tipoVariable, tipoDec, tipoValor, id, ts,exp):
    #print("-------------------Declaracion con tipo y con valor-------------------")
    
    #print("tipovariable",tipoVariable)
    # print("tipodeclaracion", tipoDec)
    #print("tipovalor", tipoValor) 
    
    
    if tipoVariable == "number" and tipoValor is type(1):
        simbolo = Simbolos(id, TIPO_DATO.ENTERO, exp)
        ts.agregar(simbolo)
    elif tipoVariable == "float" and tipoValor is type(1.1):
        simbolo = Simbolos(id, TIPO_DATO.DECIMAL, exp)
        ts.agregar(simbolo)
    elif tipoVariable == "float" and tipoValor is type(1):
        simbolo = Simbolos(id, TIPO_DATO.DECIMAL, float(exp))
        ts.agregar(simbolo)
    elif tipoVariable == "boolean" and tipoValor is type(True):
        simbolo = Simbolos(id, TIPO_DATO.BOOLEAN, exp)
        ts.agregar(simbolo)
    elif tipoVariable == "string" and tipoValor is type(""):
        simbolo = Simbolos(id, TIPO_DATO.STRING, exp)
        ts.agregar(simbolo)
    elif tipoVariable == "char" and tipoValor is type(""):
        simbolo = Simbolos(id, TIPO_DATO.CHAR, exp)
        ts.agregar(simbolo)
    elif tipoVariable =="number[]" and tipoValor is type([]):
        
        array = []
        for i in exp:

            if type(i) is type(1):
                array.append(i)
            else:
                print("Error: tipo de dato no válido")
                ts.errores+="Error: tipo de dato no válido\n"
        
        simbolo = Simbolos(id, TIPO_DATO.ARRAY, array)
        ts.agregar(simbolo)
        
    elif tipoVariable =="float[]" and tipoValor is type([]):
        array = []
        for i in exp:
            if type(i) is type(1.1):
                array.append(i)
            else:
                print("Error: tipo de dato no válido")
                ts.errores+="Error: tipo de dato no válido\n"
        
        simbolo = Simbolos(id, TIPO_DATO.ARRAY, array)
        ts.agregar(simbolo)
        
    elif tipoVariable =="boolean[]" and tipoValor is type([]):
        array = []
        for i in exp:
            if type(i) is type(True):
                array.append(i)
            else:
                print("Error: tipo de dato no válido")
                ts.errores+="Error: tipo de dato no válido\n"
        
        simbolo = Simbolos(id, TIPO_DATO.ARRAY, array)
        ts.agregar(simbolo)
    
    elif tipoVariable =="string[]" and tipoValor is type([]):
        array = []
        for i in exp:
            if type(i) is type(""):
                array.append(i)
            else:
                print("Error: tipo de dato no válido")
                ts.errores+="Error: tipo de dato no válido\n"
        
        simbolo = Simbolos(id, TIPO_DATO.ARRAY, array)
        ts.agregar(simbolo)
    
    elif tipoVariable =="char[]" and tipoValor is type([]):
        array = []
        for i in exp:
            if type(i) is type(""):
                array.append(i)
            else:
                print("Error: tipo de dato no válido")
                ts.errores+="Error: tipo de dato no válido\n"
        
        simbolo = Simbolos(id, TIPO_DATO.ARRAY, array)
        ts.agregar(simbolo)

    elif isinstance(tipoVariable, dict):   
        valida,rows=es_matriz(exp)
        
        tipo=tipoVariable["tipo"]
        dimensionDec=tipoVariable["dimension"]
        

        #print("Procesar matriz-------------",tipo,dimensionDec,rows,valida)

        if  valida:
           
                #print("Tipo.....",tipo)
                # print("Dimension.....",dimensionDec)
                # print("Rows.....",rows)
                # print("Exp.....",exp)
                # print("Id......",id)
                
                simbolo = Simbolos(id, TIPO_DATO.MATRIZ, exp)
                ts.agregar(simbolo)
                    
                    
            # else:
            #     print("Error: Las dimensiones de la matriz no coinciden")
            #     ts.errores+="Error: Las dimensiones de la matriz no coinciden\n"
           


        else:
            print("Error: tipo de dato no válido")
            ts.errores+="Error: tipo de dato no válido\n"
            
            




    else:
        print("Error3: tipo de dato no válido",tipoValor,tipoVariable)
        ts.errores+="Error3: tipo de dato no válido\n"

def declaracion_sin_tipo_con_valor(id,tipoValor,exp,ts):
    
    if tipoValor is type(1):
        simbolo = Simbolos(id, TIPO_DATO.ENTERO, exp)
        ts.agregar(simbolo)
    elif tipoValor is type(1.1):
        simbolo = Simbolos(id, TIPO_DATO.DECIMAL, exp)
        ts.agregar(simbolo)
    elif tipoValor is type(True):
        simbolo = Simbolos(id, TIPO_DATO.BOOLEAN, exp)
        ts.agregar(simbolo)
    elif tipoValor is type("") and len(exp)>1:

       
        simbolo = Simbolos(id, TIPO_DATO.STRING, exp)
        ts.agregar(simbolo)
    elif tipoValor is type("") and len(exp)==1:
        simbolo = Simbolos(id, TIPO_DATO.CHAR, exp)
        ts.agregar(simbolo)
    elif tipoValor is type([]):
        valida,rows=es_matriz(exp)
        # print("Valida",valida)
        # print("Rows",rows)

        if valida!=None and rows!=None:
            if rows%2==0 and valida:
                simbolo = Simbolos(id, TIPO_DATO.MATRIZ, exp)
                ts.agregar(simbolo)

            elif rows%2!=0 and valida:
                print("Error: dimension de la matriz no válidas")
                ts.errores+="Error: dimension de la matriz no válidas\n"
        
        else:
            simbolo = Simbolos(id, TIPO_DATO.ARRAY, exp)
            ts.agregar(simbolo)
        
        
        

    else:
        print("Error4: tipo de dato no válido",tipoValor)
        ts.errores+="Error4: tipo de dato no válido\n"

    
    
    
def procesar_declaracion(instr, ts):
    from procesos.resolver_expresion import resolver_expresion
    
    
    id = instr.id

    exp = resolver_expresion(instr.exp, ts)
    
    tipoDec = instr.tipodec  
    tipoVariable = instr.tipovar 
    tipoValor = type(exp)

    simbolo = Simbolos(id, TIPO_DATO.ENTERO, exp)
    ts.agregar(simbolo)
    ts.dato += f'{id}: .word 0\n'
    lasttemporal = ts.lastTemporal()
    temporal = ts.generateTemporal()
    ts.salida += f'la {temporal}, {id}\n'
    ts.salida += f'sw {lasttemporal}, 0({ts.lastTemporal()})\n'

  
    
    if exp!="ERARA91":
        
        if tipoValor!=type(None) and tipoDec!=None and tipoVariable!=None and tipoDec!="const":
            #print("Declaracion con tipo y con valor***")
            declaracion_con_tipo_con_valor(tipoVariable, tipoDec, tipoValor, id, ts,exp)
            
        elif tipoValor==type(None) and tipoDec!=None and tipoVariable!=None and tipoDec!="const":
            
            #print("Declaracion con tipo y sin valor***")
            declaracion_con_tipo_sin_valor(tipoVariable, tipoDec, id, ts)
            
        elif tipoDec=="const":
            #print("Declaracion de una constante***")
            declaracion_const(exp,tipoVariable, tipoDec, tipoValor, id, ts)
            
        elif tipoVariable==None and tipoDec!=None and tipoDec!="const" :
            #---print("Declaracion sin tipo y con valor***")
            declaracion_sin_tipo_con_valor(id,tipoValor,exp,ts)
            
        else:
            print("Error5: tipo de dato no válido",type(exp),tipoDec,tipoVariable,tipoValor)
            ts.errores+="Error5: tipo de dato no válido\n"
    

def es_matriz(arr):
    # Verificar si es una lista y si tiene al menos una sublista
    if isinstance(arr, list) and len(arr) > 0:
        # Obtener la longitud de la primera sublista
        longitud_sublista = None
        for sublist in arr:
            if not isinstance(sublist, list) or len(sublist) == 0:
                return False, None  # Si alguna sublista no es una lista o está vacía, no es una matriz
            if longitud_sublista is None:
                longitud_sublista = len(sublist)
            elif len(sublist) != longitud_sublista:
                return False, None  # Si alguna sublista tiene una longitud diferente, no es una matriz
        return True, len(arr)  # Devolver verdadero y el número de filas

    return False, None

def hay_valor_incorrecto(arr, tipo_dato):
    # Verificar si es una lista y si tiene al menos una sublista
    if isinstance(arr, list) and len(arr) > 0:
        # Recorrer la matriz y buscar el valor incorrecto
        for sublist in arr:
            if isinstance(sublist, list):
                for elemento in sublist:
                    if not isinstance(elemento, tipo_dato):
                        return True  # Devolver True si encuentra un valor incorrecto
            else:
                if not isinstance(sublist, tipo_dato):
                    return True  # Devolver True si encuentra un valor incorrecto en la lista principal
    return False 


# def es_matriz(arr):
#     # Verificar si es una lista y si tiene al menos una sublista
#     if isinstance(arr, list) and len(arr) > 0:
#         # Obtener la longitud de la primera sublista
#         longitud_sublista = None
#         for sublist in arr:
#             if not isinstance(sublist, list):
#                 return False  # Si alguna sublista no es una lista, no es una matriz
#             if longitud_sublista is None:
#                 longitud_sublista = len(sublist)
#             elif len(sublist) != longitud_sublista:
#                 return False  # Si alguna sublista tiene una longitud diferente, no es una matriz
#         return True

#     return False


