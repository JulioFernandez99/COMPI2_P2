from expresiones.array import ExpresionAccesoArray, ExpresionAccesoMatriz, Vector
from expresiones.cadena import *
from expresiones.interface import AccesoStruct
from expresiones.logica import ExpresionLogica, OperacionLogica
from expresiones.numericas import *
from expresiones.relacion import Relacional
from instrucciones.instrucciones import  CallFunction, LlamadaNativaConParamtros, LlamadaNativaSinParamtros, LlamadaNativaTypeOf, Parseo
from procesos.procesar_acceso_array import procesar_acceso_array
from procesos.procesar_acceso_matriz import procesar_acceso_matriz
from procesos.procesar_asignacion_struct import procesar_asignacion_struct
from procesos.procesar_llamada_funcion import procesar_llamada_funcion
from procesos.procesar_llamada_funcion_nativa_con_parametros import procesar_llamada_funcion_nativa_con_paramtros
from procesos.procesar_llamada_funcion_nativa_sin_parametros import procesar_llamada_funcion_nativa_sin_paramtros
from procesos.procesar_parseo import procesar_parseo
from procesos.procesar_typeof import procesar_typeof
from procesos.procesar_vector import procesar_vector
from procesos.resolver_expresion_aritmetica import resolver_expresion_aritmetica
from procesos.resolver_expresion_logica import resolver_expresion_logica
from procesos.resolver_expresion_relacional import resolver_expresion_relacional


def resolver_expresion(expCad, ts) :
    
    
    if isinstance(expCad, ExpresionBinaria) :
        exp = resolver_expresion_aritmetica(expCad, ts)
        try:
            return exp
        except:
            #print("Error1: variable no declarada")
            return None
   
    elif isinstance(expCad, ExpresionDobleComilla) :
        msg = ts.generateMsg()
        cadena = expCad.val.replace('"','')
        ts.dato += f'msg{msg}: .asciz "{cadena}"\n'
        return f'msg{msg}', len(cadena)
            
    elif isinstance(expCad, ExpresionComilla):
        try:
            return expCad.val.replace("'","")
        except:
            #print("Error3: variable no declarada")
            return None
            
    elif isinstance(expCad, ExpresionID):  
        
        exp_id =  ts.obtener(expCad.id)
        if exp_id.valor is None:
            if exp_id.props is not None:
                return exp_id.props
           
        try:
            return ts.obtener(expCad.id).valor
        except:
            return None
        

    elif isinstance(expCad, ExpresionNumero):
        try:
            return expCad.val
        except:
            #print("Error4: variable no declarada")
            return None
        
    elif isinstance(expCad, ExpresionLogica):
        #print("Expresion logica--------")
        try:
            return expCad.val
        except:
            #print("Error5: variable no declarada")
            return None
        
    elif isinstance(expCad, OperacionLogica):
        exp=resolver_expresion_logica(expCad,ts)
        try:
            return exp
        except:
            #print("Error6: variable no declarada")
            return None
        
        
    elif isinstance(expCad, Relacional):
        exp=resolver_expresion_relacional(expCad,ts)
        try:
            return exp
        except:
            #print("Error6: variable no declarada")
            return None
        
    elif isinstance(expCad, ExpresionNegativo):
        exp=resolver_expresion(expCad.exp,ts)
        try:
            return exp*-1
        except:
            #print("Error6: variable no declarada")
            return None
        
    elif isinstance(expCad, ExpresionVacia):
        return ""
           
    elif isinstance(expCad, Vector):
        #print("Expresion vector--------")
        vector=procesar_vector(expCad,ts)
        return vector
        
    elif isinstance(expCad, ExpresionAccesoMatriz):  
        #print("Expresion acceso array--------")
        val=procesar_acceso_matriz(expCad,ts)
        return val
    
    elif isinstance(expCad, ExpresionAccesoArray):  
        #print("Expresion acceso array--------")
        val=procesar_acceso_array(expCad,ts)
        return val
        
    elif isinstance(expCad, Parseo):
        val=procesar_parseo(expCad,ts)
        return val
    
    elif isinstance(expCad,LlamadaNativaSinParamtros):
        val=procesar_llamada_funcion_nativa_sin_paramtros(expCad,ts)
        return val
    
    elif isinstance(expCad,LlamadaNativaConParamtros):
        val=procesar_llamada_funcion_nativa_con_paramtros(expCad,ts)
        return val
    
        
    elif isinstance(expCad, LlamadaNativaTypeOf):
        val=procesar_typeof(expCad,ts)
        return val
        
      
    elif isinstance(expCad, CallFunction):
        exp=procesar_llamada_funcion(expCad,ts)
        return exp  
    
    elif isinstance(expCad, AccesoStruct):
        val=procesar_asignacion_struct(expCad,ts)
        return val
         
   
    
    
    
       
        
        
    
    elif expCad == None:
        return None
    else:
        print('Error: Expresión cadena no válida-----',expCad)
        ts.errores+="Error: Expresión cadena no válida\n"