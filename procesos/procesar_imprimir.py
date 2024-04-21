#---------------------------------------IMPRIMIR--------------------------------------


from expresiones.cadena import ExpresionDobleComilla
from expresiones.logica import ExpresionLogica
from expresiones.numericas import ExpresionBinaria, ExpresionID, ExpresionNumero


def procesar_imprimir(instr,ts):
    from procesos.resolver_expresion import resolver_expresion



    if len(instr.cad) > 1:  
        for i in range(len(instr.cad)):
            
          
            exp, size = resolver_expresion(instr.cad[i], ts)
            

            if isinstance(instr.cad[i], ExpresionBinaria) :
                
                ts.salida += f'''la a1, {exp}
                            li a2, {size}
                            jal ra, console_log'''
            elif isinstance(instr.cad[i], ExpresionLogica):
                ts.salida += f'''la a1, {exp}
                            li a2, {size}
                            jal ra, console_log'''
            elif isinstance(instr.cad[i], ExpresionDobleComilla) :
                
                ts.salida += f'''la a1, {exp}
                                li a2, {size}
                                li a0, 1 
                                li a7, 64 
                                ecall\n'''
            elif isinstance(instr.cad[i], ExpresionID):
                
                temporal = ts.generateTemporal()
                ts.salida += f'''la {temporal}, {exp}
                                lw a0, 0({temporal})
                                li a7, 1
                                ecall\n'''
            elif isinstance(instr.cad[i], ExpresionNumero):
                ts.salida += f'''la a0, {exp}
                                li a7, 1
                                ecall\n'''
            
    else:
        
        
       
        
        if isinstance(instr.cad[0], ExpresionBinaria) :
            exp,size = resolver_expresion(instr.cad[0], ts)
            print("entro aca----")
            ts.salida += f'''la a1, {exp}
                        li a2, {size}
                        jal ra, console_log'''
        elif isinstance(instr.cad[0], ExpresionLogica):
            exp,size = resolver_expresion(instr.cad[0], ts)
            ts.salida += f'''la a1, {exp}
                        li a2, {size}
                        jal ra, console_log'''
        elif isinstance(instr.cad[0], ExpresionDobleComilla) :
            exp,size = resolver_expresion(instr.cad[0], ts)
            ts.salida += f'''la a1, {exp}
                            li a2, {size}
                            li a0, 1 
                            li a7, 64 
                            ecall\n'''
        elif isinstance(instr.cad[0], ExpresionID):
            
            temporal = ts.generateTemporal()
            ts.salida += f'''la {temporal}, {instr.cad[0].id}
                            lw a0, 0({temporal})
                            li a7, 1
                            ecall\n'''
        elif isinstance(instr.cad[0], ExpresionNumero):
            ts.salida += f'''la a0, {instr.cad[0].id}
                            li a7, 1
                            ecall\n'''

