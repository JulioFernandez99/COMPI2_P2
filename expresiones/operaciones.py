
#Aqui se definen las clases que representan las expresiones

from enum import Enum

class OPERACION_ARITMETICA(Enum):
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4
    MODULO = 5
    AUMENTO = 6
    DECREMENTO = 7

    

class OPERACION_RELACION(Enum):
    
    MAYORQUE = 1
    MENORQUE = 2
    MAYORIGUAL = 3
    MENORIGUAL = 4
    IGUALIGUAL = 5
    DIFERENTE = 6
    

class OPERACION_LOGICA(Enum):
    AND = 1
    OR = 2
    NOT = 3
    

class Parser(Enum):
    TOINT = 1
    TOFLOAT = 2


        

        

        