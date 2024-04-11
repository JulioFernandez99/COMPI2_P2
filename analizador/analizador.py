
from expresiones.array import ExpresionAccesoArray, ExpresionAccesoMatriz, Vector
from expresiones.cadena import *
from expresiones.comparacion import Comparacion
from expresiones.interface import AccesoStruct
from expresiones.numericas import *
from expresiones.operaciones import *
from expresiones.logica import *
from expresiones.relacion import Relacional
from expresiones.transferencia import SentReturn
from instrucciones.instrucciones import *

reservadas = {
    'console': 'CONSOLE',
    'log': 'LOG',
    'let': 'LET',
    'var': 'VAR',
    'const': 'CONST',
    'null' : 'NULL',
    
    'number' : 'NUMBER',
    'float' : 'FLOAT',
    'string' : 'STRING',
    'boolean' : 'BOOLEAN',
    'char' : 'CHAR',
    
    
    'true' : 'TRUE',
    'false' : 'FALSE',
    'interface' : 'INTERFACE',
    'tostring' : 'TSTRING',
    'tolowercase' : 'LC',
    'touppercase' : 'UC',
    'parseint' : 'TOINT',
    'parsefloat' : 'TOFLOAT',
    
     #Funciones nativas
    'push' : 'PUSH',
    'pop' : 'POP',
    'indexof' : 'INDEXOF',
    'join' : 'JOIN',
    'length' : 'LENGTH',
    
    'if' : 'IF',
    'else': 'ELSE',
    'continue': 'CONTINUE',
    'while': 'WHILE',
    'for': 'FOR',
    'of': 'OF',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'function': 'FUNCTION',
    'typeof': 'TYPEOF',
    'interface': 'INTERFACE',
    'return': 'RETURN',
    'break': 'BREAK'

}

# Lista de tokens
tokens = [
    'PARENI',
    'PAREND',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'PUNTO',
    'PUNTOCOMA',
    'DOSPUNTOS',
    'COMA',
    'CADENA',
    'ENTERO',
    'DECIMAL',
    'COMMENTBLOCK',
    'ID',
    'IGUAL',
    'CARACTER',
    'COMILLAS',
    'BARRAINVERTIDA',
    'MOD',
    'AND',
    'OR',
    'NOT',
    'AUMENTO',
    'DECREMENTO',
    'MENORQ',
    'MAYORQ',
    'MENORIGUALQ',
    'MAYORIGUALQ',
    'IGUALIGUAL',
    'DIFERENTE',
    'LLAVEI',
    'LLAVED',
    'CORCHETEI',
    'CORCHETED',
    'VACIO',
    'INCREMENTOFOR',
    'DECREMENTOFOR',
    
    
] + list(reservadas.values())

t_CONSOLE  = r'console'
t_LOG  = r'log'
t_LET  = r'let'
t_IF  = r'if'
t_DOSPUNTOS = r':'
t_IGUAL     = r'='
t_PARENI    = r'\('
t_PAREND    = r'\)'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_PUNTO    = r'\.'
t_PUNTOCOMA    = r';'
t_COMA   = r'\,'
t_COMILLAS = r'\"'
t_BARRAINVERTIDA = r'\\'
t_MOD = r'%'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_AUMENTO = r'\+='
t_DECREMENTO = r'-='

t_MENORQ = r'<'
t_MAYORQ = r'>'
t_MENORIGUALQ = r'<='
t_MAYORIGUALQ = r'>='
t_IGUALIGUAL = r'=='
t_DIFERENTE = r'!='
t_LLAVEI = r'{'
t_LLAVED = r'}'
t_CORCHETEI = r'\['
t_CORCHETED = r'\]'
t_VACIO = r'\"\"'
t_INCREMENTOFOR = r'\+\+'
t_DECREMENTOFOR = r'--'





def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t

def t_CARACTER(t):
    r'\'[a-zA-Z]\''
    try:
        t.value = str(t.value)
    except ValueError:
        print("Error %d", t.value)
        t.value = ''
    return t
    
def t_TOLOWER(t):
    r'toLowerCase'
    t.type = reservadas.get(t.value.lower(), 'LC')
    return t

def t_CADENA(t):
    r'\"(.+?)\"'
    t.value=t.value[1:-1]
    
    try:
        t.value = str(t.value)
    except ValueError:
        print("Error %d", t.value)
        t.value = ''
    return t



def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


t_ignore = " \t"

t_ignore_COMMENTLINE = r'\/\/.*'

def t_ignore_COMMENTBLOCK(t):
    r'\/\*[^*]*\*+(?:[^/*][^*]*\*+)*\/'
    t.lexer.lineno += t.value.count('\n')  


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Error Léxico '%s'" % t.value[0])
    t.lexer.skip(1)


precedence = (
        ('left', 'MAS', 'MENOS'),
        ('left', 'POR', 'DIVIDIDO' ),
        ('right', 'AUMENTO', 'DECREMENTO', 'INCREMENTOFOR', 'DECREMENTOFOR'),
        ('left', 'OR','AND'),
        ('left', 'MENORQ', 'MAYORQ', 'MAYORIGUALQ', 'MENORIGUALQ'),
        ('left', 'IGUALIGUAL', 'DIFERENTE' ),
        ('left', 'MOD'),
        ('left', 'PARENI', 'PAREND'),
        ('left', 'LLAVEI', 'LLAVED'),
        ('right', 'NOT'),
        ('left', 'PUNTO'),
        ('right', 'UMENOS')
    )




def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t):
    '''instrucciones    : instrucciones instruccion'''
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_instruccion(t) :
    '''instruccion      : imprimir PUNTOCOMA
                        | declaracion PUNTOCOMA
                        | asignacion PUNTOCOMA
                        | if_instr 
                        | if_else_instr 
                        | if_elseif_instr 
                        | if_elseif_else_instr
                        | for_instr
                        | while_instr
                        | switch_instr
                        | llamada_funcion_nativa PUNTOCOMA
                        | funcion_instr  
                        | call_funcion_instr PUNTOCOMA
                        | interface_instr
                        | delaracion_struct
                        | return_instr
                        | break_instr      
                        | continue_instr                  
                        
                        
                        
    '''
    t[0] = t[1]
    

def p_tipo_declaracion(t):
    '''tipodeclaracion : LET
            | VAR
            | CONST'''
    t[0] = t[1]

def p_corchetes_matriz(t):
    '''lista_corchetes : lista_corchetes CORCHETEI CORCHETED 
                        | CORCHETEI CORCHETED CORCHETEI CORCHETED'''
    
    #verificar que la cantidad de corchetes sea par
    
    if len(t) > 4:
        t[0]=2
        
    else:
        t[0]=t[1]+1
        
   
    # if t[0]%2==0:
    #     print("Cantidad de corchetes correcta",t[0])
        
    # else:
    #     print("Error: dimension de matriz incorrecta ")

    

    
  

    

    

def p_tipo_variable(t):
    '''tipovar : NUMBER
            | FLOAT
            | STRING
            | BOOLEAN
            | CHAR
            | NUMBER CORCHETEI CORCHETED
            | FLOAT CORCHETEI CORCHETED
            | STRING CORCHETEI CORCHETED
            | BOOLEAN CORCHETEI CORCHETED
            | CHAR CORCHETEI CORCHETED

            | NUMBER lista_corchetes
            | FLOAT lista_corchetes
            | STRING lista_corchetes
            | BOOLEAN lista_corchetes
            | CHAR lista_corchetes
    '''
  
    if len(t) == 4:
        t[0] = t[1] + '[]'

    elif len(t) == 3:
        
        t[0] = {
            "tipo":t[1],
            "dimension":t[2]
            }
        
    else:
        t[0] = t[1]
     
def p_instruccion_console(t):
    '''imprimir : CONSOLE PUNTO LOG PARENI  listaExpresiones PAREND '''
    t[0] = Imprimir(t[5])
    
def p_lista_expresiones(t):
    """
    listaExpresiones :  listaExpresiones COMA expresion
                    | expresion
                    
    """
    if len(t) > 2:
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]
        
def p_array_con_valores(t):
    """
    arraylist : CORCHETEI listaExpresiones CORCHETED
    """
    t[0] = t[2]
    
def p_array_vacio(t):
    """
    arraylist : CORCHETEI CORCHETED
    """
    t[0] = []

def p_expresion_array(t):
    """
    expresion : arraylist
    """
    t[0] = Vector(t[1])
    

#---------------------DECLARACION---------------------
def p_instruccion_declaracion_con_tipo_valor(t):
    '''declaracion : tipodeclaracion ID DOSPUNTOS tipovar IGUAL expresion '''
    #print("-------------entro",t[4])
    t[0] = Declaracion(t[2], t[6], t[4],t[1])
                    #  id ,  exp, tipovar, tipodec


def p_instruccion_declaracion_con_valor(t):
    '''declaracion : tipodeclaracion ID IGUAL expresion '''
    t[0] = Declaracion(t[2], t[4], None, t[1])
                     #  id ,  exp, tipovar, tipodec

def p_instruccion_declaracion_con_tipo_sin_valor(t):
   
    '''declaracion : tipodeclaracion ID DOSPUNTOS tipovar '''
    
    t[0] = Declaracion(t[2], None, t[4],t[1])
     
#---------------------ASIGNACION---------------------

def p_instruccion_asignacion(t):    
    '''asignacion : ID IGUAL expresion '''
    print
    t[0] = Asignacion(t[1], t[3])
    
def p_instruccion_posicion_array(t):
    '''asignacion : ID CORCHETEI expresion CORCHETED IGUAL expresion '''
    t[0] = AsignacionPosicionArray(t[1],t[3],t[6])

def p_instruccion_posicion_matriz(t):
    '''asignacion : ID pos_matriz IGUAL expresion '''
    t[0] = AsignacionPosicionMatriz(t[1],t[2],t[4])
    
def p_instruccion_operador_asignacion(t):
    '''asignacion : ID AUMENTO expresion 
                  | ID DECREMENTO expresion 
    '''
    if t[2] == '+=':
        t[0] = AsignacionOperador(t[1],t[3],OPERACION_ARITMETICA.MAS)
    elif t[2] == '-=':
        t[0] = AsignacionOperador(t[1],t[3],OPERACION_ARITMETICA.MENOS)
    
    
    
#---------------------IF---------------------
def p_lista_if(t):
    """
    listaIf :  listaIf elseIF
                    | elseIF
    """
    if len(t) > 2:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]  

def p_else_if(t):
    """
    elseIF : ELSE if_instr
    """
    t[0] = t[2] 


def p_if_instr(t) :
    'if_instr           : IF PARENI expresion PAREND LLAVEI instrucciones LLAVED'
    t[0] = If(t[3], t[6])


    
def p_if_else_instr(t) :
    'if_else_instr      : IF PARENI expresion PAREND LLAVEI instrucciones LLAVED ELSE LLAVEI instrucciones LLAVED'
    t[0] = IfElse(t[3], t[6], t[10])
 
def p_if_elseif_instr(t):
    '''
    if_elseif_instr   : IF PARENI expresion PAREND LLAVEI instrucciones LLAVED listaIf 
    '''   
    t[0] = Elif(t[3], t[6],t[8])
 
def p_if_elseif_else_instr(t):
    '''
    if_elseif_else_instr   : IF PARENI expresion PAREND LLAVEI instrucciones LLAVED listaIf ELSE LLAVEI instrucciones LLAVED
    '''   
   
    t[0] = Elif_ELSE(t[3], t[6],t[8],t[11])   
    
#-------------------------FOR Normal-------------------------

def p_for_instr_incremento(t) :
    'actualizacion        : ID INCREMENTOFOR'
    t[0] = ACTUALIZACIONFOR(t[1], OPERACION_ARITMETICA.AUMENTO)

def p_for_instr_decremento(t) :
    'actualizacion        : ID DECREMENTOFOR'
    t[0] = ACTUALIZACIONFOR(t[1], OPERACION_ARITMETICA.DECREMENTO)
       

def p_for_instr(t) :
    'for_instr        : FOR PARENI declaracion PUNTOCOMA expresion PUNTOCOMA actualizacion PAREND LLAVEI instrucciones LLAVED'
    t[0] = For(t[3], t[5], t[7], t[10])
    
#----------------------------------------------------------

#--------------------------FOR OF--------------------------
def p_for_of_instr(t) :
    'for_instr        : FOR PARENI tipodeclaracion ID OF ID PAREND LLAVEI instrucciones LLAVED'
    t[0] = ForOf(t[4], t[6], t[9])
#----------------------------------------------------------

#---------------------WHILE---------------------
def p_while_instr(t) :
    'while_instr        : WHILE PARENI expresion PAREND LLAVEI instrucciones LLAVED'
    t[0] = While(t[3], t[6])
#-------------------------------------------------

#---------------------SWITCH---------------------
def p_lista_cases(t):
    """
    listaCases : listaCases case
                    | case
    """
    if len(t) > 2:
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

def p_case(t):
    """
    case : CASE expresion DOSPUNTOS instrucciones
    """
    t[0] = Case(t[2], t[4])
    
def p_case_default(t):
    """
    case : DEFAULT DOSPUNTOS instrucciones
    """
    t[0] = Case(None, t[3])

def p_switch_instr(t) :
    'switch_instr        : SWITCH PARENI expresion PAREND LLAVEI listaCases LLAVED'
    t[0] = Switch(t[3], t[6])
#-------------------------------------------------


#---------------------FUNCIONES NATIVAS---------------------

def p_funciones_embedidas_sin_parametros(t):
    '''
        nativa_sin_parametros :     POP PARENI PAREND
                                  | JOIN PARENI PAREND
                                  | TSTRING PARENI PAREND
                                  | LC PARENI PAREND
                                  | UC PARENI PAREND
                                  | LENGTH
                                  
    '''
    t[0] = t[1]

def p_funciones_embedidas_con_parametros(t):
    '''
        llamada_funcion_nativa :    PUSH
                                  | INDEXOF
    '''
    t[0] = t[1]

def p_llamada_funcion_nativa_sin_parametros(t):
    '''
        llamada_funcion_nativa :    expresion PUNTO nativa_sin_parametros
    '''
    t[0] = LlamadaNativaSinParamtros(t[1], t[3])


def p_llamada_funcion_nativa_con_parametros(t):
    '''
        llamada_funcion_nativa :    expresion PUNTO llamada_funcion_nativa PARENI listaExpresiones PAREND
    '''
    t[0] = LlamadaNativaConParamtros(t[1], t[3], t[5])
    
def p_llamada_funcion_nativa_typeof(t):
    '''
        llamada_funcion_nativa :    TYPEOF expresion
    '''
    t[0] = LlamadaNativaTypeOf(t[2])

#---------------------------------------------------------------

#-----------------------------Funciones embebidas----------------------------

def p_expresion_llamada_funcion_nativa(t):
    '''expresion : llamada_funcion_nativa'''
    t[0] = t[1]


def p_funcion_embebida_to_int(t):
    '''expresion : TOINT PARENI expresion PAREND'''
    # numero_redondeado = int(round(float(t[3].val)))
    # t[0] = ExpresionNumero("int",numero_redondeado)
    t[0]=Parseo(t[1],t[3])
    

def p_funcion_embebida_to_float(t):
    '''expresion : TOFLOAT PARENI expresion PAREND'''
    # numero_redondeado = round(float(t[3].val),2)
    # print("entro a tofloat",numero_redondeado)
    # t[0] = ExpresionNumero("float",numero_redondeado)
    t[0]=Parseo(t[1],t[3])
    
    
#----------------------------------------------------------------------------
    
#----------------------------FUNCIONES------------------------
def p_parametros_funcion(t):
    """
    parametros_funcion : parametros_funcion COMA parametro_funcion
                    | parametro_funcion
    """
    if len(t) > 2:
        t[1].append(t[3])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

def p_parametros_funcion_var(t):
    """
    parametro_funcion : ID DOSPUNTOS tipovar
    """
    t[0] = Parametro(t[1],t[3])
    
def p_parametros_funcion_arr(t):
    """
    parametro_funcion : ID DOSPUNTOS tipovar CORCHETEI  CORCHETED
    """
    t[0] = Parametro(t[1],t[3])


#--------------------------------Call Funcion--------------------------------
def  p_call_funcion_instr(t) :
    'call_funcion_instr      : ID PARENI PAREND'
    t[0] = CallFunction(t[1])
    
def  p_call_funcion_instr_params(t) :
    'call_funcion_instr      : ID PARENI listaExpresiones PAREND'
    #print("entro a llamada de funcion con parametros------")
    t[0] = CallFunction(t[1],t[3])
#---------------------------------------------------------------------------

#--------------------------Funcion que no retorna nada----------------------

def  p_funcion_con_parametros_instr(t) :
    'funcion_instr      : FUNCTION ID PARENI parametros_funcion  PAREND LLAVEI instrucciones LLAVED'
    #print("entro a funcion con parametros")
    t[0] = Function(t[2],parametros=t[4],instrucciones=t[7])


def  p_funcion_instr(t) :
    'funcion_instr      : FUNCTION ID PARENI PAREND LLAVEI instrucciones LLAVED'
    #print("entro a funcion sin parametros")
    t[0] = Function(t[2],instrucciones=t[6])

#----------------------------------------------------------------------  

#--------------------------Funcion que retorna algo----------------------

def  p_funcion_con_parametros_instr_retorno(t) :
    'funcion_instr      : FUNCTION ID PARENI parametros_funcion  PAREND DOSPUNTOS tipovar  LLAVEI instrucciones LLAVED'
    #print("entro a funcion con parametros",t[7])
    t[0] = Function(t[2],parametros=t[4],instrucciones=t[9],retorno=t[7])


def  p_funcion_instr_retorno(t) :
    'funcion_instr      : FUNCTION ID PARENI PAREND DOSPUNTOS tipovar LLAVEI instrucciones LLAVED'
    #print("entro a funcion sin parametros")
    t[0] = Function(t[2],instrucciones=t[8],retorno=t[6])

#----------------------------------------------------------------------  

#----------------------------------Interfaces--------------------------------

def p_instruccion_interface(t):
    '''interface_instr : INTERFACE ID LLAVEI interface_params PUNTOCOMA LLAVED'''

    t[0] = Interface(t[2],t[4])

def p_instruccion_interface_params(t):
    '''interface_params : interface_params PUNTOCOMA ID DOSPUNTOS tipovar
                        | ID DOSPUNTOS tipovar'''
    if(len(t) == 4):
        t[0] = {t[1]: t[3]} 
    else:
        t[1][t[3]] = t[5]
        t[0] = t[1]
            

def p_expresion_struct(t):
    '''delaracion_struct : expresion PUNTO expresion IGUAL expresion PUNTOCOMA'''
    t[0] = AccesoStruct(t[1], t[3], t[5])
 
    
def p_acceso_struct(t):
    '''expresion : expresion PUNTO expresion '''
    t[0] = AccesoStruct(t[1], t[3])    
    

    



#------------------------------------------------------------------------------



#------------------------------------Return--------------------------------------
def p_instruccion_retorno(t):
    '''return_instr     : RETURN expresion PUNTOCOMA
                        | RETURN PUNTOCOMA'''
    if len(t) == 4:
        t[0] = ReturnInstr(t[2])
    else:
        t[0] = ReturnInstr(None)


#------------------------------------Break--------------------------------------
def p_instruccion_break(t):
    '''break_instr     : BREAK PUNTOCOMA'''
    t[0] = BreakInstr()

#------------------------------------Continue--------------------------------------
def p_instruccion_continue(t):
    '''continue_instr     : CONTINUE PUNTOCOMA'''
    t[0] = ContinueInstr()
#------------------------------------Expresiones---------------------------------

def p_expresion_call_funcion(t):
    '''expresion : call_funcion_instr'''
    t[0] = t[1]

def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIVIDIDO expresion
                  | expresion MOD expresion'''
                  
    if t[2] == '+'  : t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == '-': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
    elif t[2] == '/': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)
    elif t[2] == '%': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MODULO)
    

def p_expresion_relacional(t):
    '''expresion : expresion MENORQ expresion
                  | expresion MAYORQ expresion
                  | expresion MAYORIGUALQ expresion
                  | expresion MENORIGUALQ expresion
                  | expresion IGUALIGUAL expresion
                  | expresion DIFERENTE expresion            
    '''
    if t[2] == '>'  : t[0] = Relacional(t[1], t[3], OPERACION_RELACION.MAYORQUE)
    elif t[2] == '<': t[0] = Relacional(t[1], t[3], OPERACION_RELACION.MENORQUE)
    elif t[2] == '>=': t[0] = Relacional(t[1], t[3], OPERACION_RELACION.MAYORIGUAL)
    elif t[2] == '<=': t[0] = Relacional(t[1], t[3], OPERACION_RELACION.MENORIGUAL)
    elif t[2] == '==': t[0] = Relacional(t[1], t[3], OPERACION_RELACION.IGUALIGUAL)
    elif t[2] == '!=': t[0] = Relacional(t[1], t[3], OPERACION_RELACION.DIFERENTE)

def p_expresion_logica(t):
    '''expresion : expresion AND expresion
                  | expresion OR expresion
                  | NOT expresion'''
                  
    if t[2] == '&&': t[0] = OperacionLogica(t[1], t[3], OPERACION_LOGICA.AND)
    elif t[2] == '||': t[0] = OperacionLogica(t[1], t[3], OPERACION_LOGICA.OR)
    elif t[1] == '!': t[0] = OperacionLogica(t[2], None, OPERACION_LOGICA.NOT)

def p_expresion_agrupacion(t):
    'expresion : PARENI expresion PAREND'
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion    : ENTERO'''
 
    t[0] = ExpresionNumero("int",t[1])
    
def p_expresion_float(t):
    '''expresion    : DECIMAL'''
    t[0] = ExpresionNumero("float",t[1])
    
    
def p_expresion_false(t):
    '''expresion : FALSE'''
    t[0] =  ExpresionLogica(False)

def p_expresion_true(t):
    '''expresion : TRUE'''
    
    t[0] =  ExpresionLogica(True)
    
def p_expresion_cadena(t):
    '''expresion    : CADENA'''
    t[0] = ExpresionDobleComilla(t[1])
    
def p_expresion_caracter(t):
    '''expresion    : CARACTER'''
    t[0] = ExpresionComilla(t[1])

def p_expresion_id(t):
    '''expresion    : ID'''
    t[0] = ExpresionID(t[1])
    

    
def p_expresion_vacio(t):
    '''expresion    : VACIO'''
    t[0] = ExpresionVacia(t[1])

def p_posiciones_matriz(t):
    '''pos_matriz : pos_matriz CORCHETEI expresion CORCHETED
                    | CORCHETEI expresion CORCHETED CORCHETEI expresion CORCHETED'''
    
    if len(t) > 5:
        
        t[0]=[t[2]]
        t[0].append(t[5])
    else:
        t[1].append(t[3])
        t[0] = t[1]

    

def p_expresion_acceso_matriz(t):
    '''expresion : ID pos_matriz'''
    #print("entro a acceso matriz-------------",t[2])
    t[0] = ExpresionAccesoMatriz(t[1], t[2])
    
def p_expresion_acceso_array(t):
    '''expresion : ID CORCHETEI expresion CORCHETED'''
    
    t[0] = ExpresionAccesoArray(t[1], t[3])
    
def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec UMENOS'
    t[0] = ExpresionNegativo(t[2])
    
def p_error(p):
    if p:
        # if p.value in reservadas.keys():
        #     print(f"Error de sintaxis,de utilizo una palabra reservada {p.lineno}, columna {p.lexpos}: Palabra reservada '{p.value}'")
             
        print(f"Error de sintaxis en línea {p.lineno}, columna {p.lexpos}: Token inesperado '{p.value}'")
    else:
        print("Error de sintaxis")

import ply.lex as Lex
import ply.yacc as yacc
lexer = Lex.lex()
parser = yacc.yacc()

#enviar una cadena al lexer he imprimir los tokens
# cadean = '''
#            console.log("Hola Mundo :D",10.1);
#     '''
# lexer.input(cadean)

# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)



        



def parse(input) :
    return parser.parse(input)