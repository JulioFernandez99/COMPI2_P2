    
class ExpresionLogica():
    def __init__(self, val):
        self.val = val
        self.tipo = "boolean"
        
class OperacionLogica():
    def __init__(self, exp1, exp2, operador):
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador