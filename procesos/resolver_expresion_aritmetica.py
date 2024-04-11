
from expresiones.cadena import *

from expresiones.interface import AccesoStruct
from expresiones.numericas import *
from expresiones.operaciones import OPERACION_ARITMETICA
from procesos.procesar_asignacion_struct import procesar_asignacion_struct


def resolver_expresion_aritmetica(expNum, ts) :
    from procesos.resolver_expresion import resolver_expresion
   
    
    # if isinstance(expNum.exp1, ExpresionID) or isinstance(expNum.exp2, ExpresionID) or isinstance(expNum.exp1, ExpresionComilla) or isinstance(expNum.exp2, ExpresionComilla):
    #     return concatenar_cadenas(expNum,ts)
        
    
    if isinstance(expNum, ExpresionBinaria) :
        
        
        exp1=resolver_expresion(expNum.exp1,ts)
        exp2=resolver_expresion(expNum.exp2,ts)
            
        if expNum.operador == OPERACION_ARITMETICA.MAS : return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.MENOS : return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.POR : return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO : 
            val=exp1 / exp2
            #print("exp1",exp1)
            #print("exp2",exp2)
            

            if exp2==0:
                print("No se puede dividir entre 0")
                ts.errores+="No se puede dividir entre 0\n"
                return "ERARA91"


            
            if isinstance(exp1, int) and isinstance(exp2, int) :
                return round(exp1 / exp2)
        
           
            return exp1 / exp2
        if expNum.operador == OPERACION_ARITMETICA.MODULO : return exp1 % exp2
        
    elif isinstance(expNum, ExpresionNumero) :return expNum.val
    elif isinstance(expNum, ExpresionID): return ts.obtener(expNum.id).valor
    elif isinstance(expNum, ExpresionNegativo) : return -1 * resolver_expresion_aritmetica(expNum.exp, ts)
    
    elif isinstance(expNum, AccesoStruct):
        return procesar_asignacion_struct(expNum,ts)
    



    
