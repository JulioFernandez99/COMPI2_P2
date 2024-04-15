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
                print("--------------------IMPRIMIR------------------")
                ts.salida += f'''la a1, {exp}
                                li a2, {size}
                                li a0, 1 
                                li a7, 64 
                                ecall\n'''
            elif isinstance(instr.cad[i], ExpresionID):
                temporal = ts.generateTemporal()
                ts.salida += f'''la t{temporal}, {exp}
                                lw a0, 0(t{temporal})
                                li a7, 1
                                ecall\n'''
            elif isinstance(instr.cad[i], ExpresionNumero):
                ts.salida += f'''la a0, {exp}
                                li a7, 1
                                ecall\n'''
            
    else:
        exp, size = resolver_expresion(instr.cad[0], ts)

        if isinstance(instr.cad[0], ExpresionBinaria) :
            ts.salida += f'''la a1, {exp}
                        li a2, {size}
                        jal ra, console_log'''
        elif isinstance(instr.cad[0], ExpresionLogica):
            ts.salida += f'''la a1, {exp}
                        li a2, {size}
                        jal ra, console_log'''
        elif isinstance(instr.cad[0], ExpresionDobleComilla) :
            print("--------------------IMPRIMIR------------------")
            ts.salida += f'''la a1, {exp}
                            li a2, {size}
                            li a0, 1 
                            li a7, 64 
                            ecall\n'''
        elif isinstance(instr.cad[0], ExpresionID):
            temporal = ts.generateTemporal()
            ts.salida += f'''la t{temporal}, {exp}
                            lw a0, 0(t{temporal})
                            li a7, 1
                            ecall\n'''
        elif isinstance(instr.cad[0], ExpresionNumero):
            ts.salida += f'''la a0, {exp}
                            li a7, 1
                            ecall\n'''

