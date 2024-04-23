
from procesos.resolver_expresion import resolver_expresion
from procesos.resolver_expresion_aritmetica import resolver_expresion_aritmetica
from procesos.resolver_expresion_relacional import resolver_expresion_relacional



def procesar_while(instr, ts):
    from procesos.procesar_instrucciones import procesar_instrucciones

    ciclo = f'L{ts.generateLabel()}'

    ts.salida += f'{ciclo}:\n' #WHILE 
    #ts.salida += f'{vars(instr.expLogica)}\n'
    expLog = resolver_expresion(instr.expLogica, ts) #SI VERDADERO EJECUTA
    
    caso_falso = f'L{ts.generateLabel()}'
    ts.salida += f'j {caso_falso}\n'

    ts.salida += f'{expLog}:\n'
    procesar_instrucciones(instr.instrucciones,ts)
    ts.salida += f'j {ciclo}\n'

    ts.salida += f'{caso_falso}:\n'

       
        
        