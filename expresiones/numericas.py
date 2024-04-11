class ExpresionNumerica:
    '''
        Esta clase representa una expresión numérica
    '''

class ExpresionBinaria(ExpresionNumerica):

    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionNumero(ExpresionNumerica):
 
    def __init__(self, tipo,val = 0) :
        self.val = val
        self.tipo = tipo
        

class ExpresionID(ExpresionNumerica):
    def __init__(self, id) :
        self.id = id
        self.tipo = "id"
        
class ExpresionNegativo(ExpresionNumerica) :
    def __init__(self, exp) :
        self.exp = exp
        
class ExpresionAccesoInterface(ExpresionNumerica):
    def __init__(self, id, prop) :
        self.id = id
        self.prop = prop