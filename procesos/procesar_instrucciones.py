#Aqui se van a recibir recibir las instrucciones y prepararlas 

from expresiones.interface import AccesoStruct
from expresiones.transferencia import SentReturn
from procesos.guardar_funcion import guardar_funcion
from procesos.guardar_interface import guardar_interface
from procesos.procesar_asigancion_matriz import procesar_asignacion_posicion_matriz
from procesos.procesar_asignacion_posicion_array import procesar_asignacion_posicion_array
from procesos.procesar_asignacion_struct import procesar_asignacion_struct
from procesos.procesar_break import procesar_break
from procesos.procesar_continue import procesar_continue
from procesos.procesar_declaracion import procesar_declaracion
from procesos.procesar_elif import procesar_if_elif
from procesos.procesar_elif_else import procesar_if_elif_else
from procesos.procesar_for import procesar_for
from procesos.procesar_for_of import procesar_for_of
from procesos.procesar_funcion import procesar_funcion
from procesos.procesar_if import procesar_if
from procesos.procesar_if_else import procesar_if_else
from procesos.procesar_imprimir import procesar_imprimir
from procesos.procesar_asignacion import procesar_asignacion, procesar_asignacion_operador
from procesos.procesar_llamada_funcion_nativa_con_parametros import procesar_llamada_funcion_nativa_con_paramtros
from procesos.procesar_llamada_funcion_nativa_sin_parametros import procesar_llamada_funcion_nativa_sin_paramtros
from procesos.procesar_retorno import procesar_retorno
from procesos.procesar_switch import procesar_switch
from procesos.procesar_while import procesar_while
from procesos.resolver_expresion_aritmetica import *
from tabla.tablaSimbolos import *
from expresiones.operaciones import *
from instrucciones.instrucciones import *

def procesar_instrucciones(instrucciones, ts,save=False) :
    
    for instr in instrucciones :
        
        
        if not save and ts.existContinue==False and ts.existBreak==False:
            
            if isinstance(instr, Imprimir) : procesar_imprimir(instr,ts)
            elif isinstance(instr, Declaracion): procesar_declaracion(instr, ts)
            elif isinstance(instr, Asignacion): procesar_asignacion(instr, ts)
            elif isinstance(instr, AsignacionOperador):procesar_asignacion_operador(instr, ts)
            elif isinstance(instr,AsignacionPosicionArray):procesar_asignacion_posicion_array(instr,ts)
            elif isinstance(instr,AsignacionPosicionMatriz):procesar_asignacion_posicion_matriz(instr,ts)
            elif isinstance(instr, If): procesar_if(instr, ts)
            elif isinstance(instr, IfElse): procesar_if_else(instr, ts)
            elif isinstance(instr, Elif): procesar_if_elif(instr, ts)
            elif isinstance(instr, Elif_ELSE): procesar_if_elif_else(instr, ts)
            elif isinstance(instr, For): procesar_for(instr, ts)
            elif isinstance(instr, ForOf): procesar_for_of(instr, ts)
            elif isinstance(instr, While): procesar_while(instr, ts)
            elif isinstance(instr, Switch): 
                
                procesar_switch(instr, ts)
            elif isinstance(instr, LlamadaNativaSinParamtros): procesar_llamada_funcion_nativa_sin_paramtros(instr, ts)
            elif isinstance(instr, LlamadaNativaConParamtros): procesar_llamada_funcion_nativa_con_paramtros(instr, ts)
            elif isinstance(instr,CallFunction): valReturn=procesar_funcion(instr, ts)
            elif isinstance(instr,AccesoStruct): procesar_asignacion_struct(instr,ts)
            elif isinstance(instr,ReturnInstr): return procesar_retorno(instr, ts), instr
            elif isinstance(instr,BreakInstr):  procesar_break(instr, ts)
            elif isinstance(instr,ContinueInstr): procesar_continue(instr, ts)
            elif isinstance(instr,Function): pass
            elif isinstance(instr,Interface): pass
            else : 
                print('Error: instrucción no válida----',)
                ts.errores+="Error: instrucción no válida\n"

        else:       
            
            if isinstance(instr, Function): guardar_funcion(instr, ts)
            elif isinstance(instr, Interface): guardar_interface(instr, ts)
                
  