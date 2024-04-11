class Transferencia():
    '''
        Clase abstracta de sentencias de transferencia
    '''
    
class SentBreak(Transferencia):
    def __init__(self, origen=''):
        self.origen = origen
        
class SentContinue(Transferencia):
    def __init__(self, origen=''):
        self.origen = origen
        
class SentReturn(Transferencia):
    def __init__(self, exp):
        self.exp = exp