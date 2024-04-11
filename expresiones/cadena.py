class ExpresionCadena:
    ''' Clase abstracta para cadenas'''

class ExpresionDobleComilla(ExpresionCadena):

    def __init__(self, val) :
        
        self.val = val
        self.tipo = "string"
        
class ExpresionComilla(ExpresionCadena):

    def __init__(self, val) :
        self.val = val
        self.tipo = "char"
        
class ExpresionVacia(ExpresionCadena):

    def __init__(self, val) :
        self.val = val
        self.tipo = ""
        