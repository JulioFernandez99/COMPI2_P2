from enum import Enum

class TIPO_DATO(Enum):
    ENTERO = 1
    DECIMAL = 2
    STRING = 3
    BOOLEAN = 4
    CHAR = 5
    ARRAY = 6
    FUNCION=7
    MATRIZ=8

class Simbolos(): #VALOR - NODO
    
    def __init__(self, id, tipo, valor,constante=False,instrucciones = [], parametros = [],tipoRetorno=None,props = {}):
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.constante = constante
        
        self.instrucciones = instrucciones
        self.parametros = parametros
        self.tipoRetorno = tipoRetorno
        self.props = props
        


class TablaSimbolos():

    def __init__(self, simbolos = {}, salida="",errores="",existBreak=False,existContinue=False,dato=''):
        self.simbolos = simbolos
        self.salida = salida
        self.dato = dato
        self.errores = errores 
        self.existBreak=existBreak
        self.existContinue=existContinue 
        self.temporal = -1
        self.label = -1
        self.msg = -1


    def agregar(self, simbolo):
        self.simbolos[simbolo.id] = simbolo

    def obtener(self, id):
        if not id in self.simbolos:
            print('Error:variable no declarada')
            self.errores += 'Error:variable no declarada\n'
            
            
        else:
            return self.simbolos[id]
    
    def actualizar(self, id, valor):
        if not id in self.simbolos:
            print('Error:variable no declarada')
        else:
            self.simbolos[id].valor = valor


    def generateTemporal(self):
        self.temporal += 1
        if self.temporal == 7:
            self.temporal = 0
        return self.temporal
    
    def lastTemporal(self):
        return self.temporal

    def generateLabel(self):
        self.label += 1
        return self.label
    
    def lastLabel(self):
        return self.label
    
    def generateMsg(self):
        self.msg += 1
        return self.msg
    
    def lastMsg(self):
        return self.msg