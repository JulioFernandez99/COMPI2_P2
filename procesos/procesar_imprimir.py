#---------------------------------------IMPRIMIR--------------------------------------


from expresiones.array import ExpresionAccesoArray, ExpresionAccesoMatriz, Vector
from expresiones.cadena import ExpresionDobleComilla
from expresiones.logica import ExpresionLogica
from expresiones.numericas import ExpresionBinaria, ExpresionID, ExpresionNumero
from procesos.resolver_expresion_aritmetica import resolver_expresion_aritmetica


def procesar_imprimir(instr,ts):
    from procesos.resolver_expresion import resolver_expresion


    
    if len(instr.cad) > 1:  
        
        for i in range(len(instr.cad)):
            
          
           
            

            if isinstance(instr.cad[i], ExpresionBinaria) :
               
                exp, size = resolver_expresion(instr.cad[i], ts)
                ts.salida += f'''la a1, {exp}
                            li a2, {size}
                            jal ra, console_log'''
            elif isinstance(instr.cad[i], ExpresionLogica):
                exp, size = resolver_expresion(instr.cad[i], ts)
                ts.salida += f'''la a1, {exp}
                            li a2, {size}
                            jal ra, console_log'''
            elif isinstance(instr.cad[i], ExpresionDobleComilla) :
                exp, size = resolver_expresion(instr.cad[i], ts)
                exp, size = resolver_expresion(instr.cad[i], ts)
                ts.salida += f'''la a1, {exp}
                                li a2, {size}
                                li a0, 1 
                                li a7, 64 
                                ecall\n'''
                
                
            elif isinstance(instr.cad[i], ExpresionID):
                

                
                
                temporal = ts.generateTemporal()
                ts.salida += f'''la {temporal}, {instr.cad[i].id}
                                lw a0, 0({temporal})
                                li a7, 1
                                ecall\n'''
                
                
            
            elif isinstance(instr.cad[i], ExpresionNumero):
                exp, size = resolver_expresion(instr.cad[i], ts)
                ts.salida += f'''la a0, {exp}
                                li a7, 1
                                ecall\n'''

        ts.salida += f'''la a1, salto
                                    li a2, 1
                                    li a0, 1 
                                    li a7, 64 
                                    ecall\n'''    
    else:
        
        
      
        if isinstance(instr.cad[0], ExpresionBinaria) :
            
            try:
                exp,size = resolver_expresion_aritmetica(instr.cad[0], ts)
                ts.salida += f'''mv a0, t{size}
                            li a7, 1
                            ecall\n'''
            except:
                exp = resolver_expresion_aritmetica(instr.cad[0], ts)
                #ts.salida+=f"Error en la expresion aritmetica {exp}"
                ts.salida += f'''mv a0, {exp}
                            li a7, 1
                            ecall\n'''

            #ts.salida += f"-----------------llegaste-----------------{size}\n"
            
            
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
            
            ts.salida += f'''la a1, salto
                                li a2, 1
                                li a0, 1 
                                li a7, 64 
                                ecall\n'''
            
        elif isinstance(instr.cad[0], ExpresionID):
            
            temporal = ts.generateTemporal()
            ts.salida += f'''la {temporal}, {instr.cad[0].id}
                            lw a0, 0({temporal})
                            li a7, 1
                            ecall\n'''
            
            ts.salida += f'''la a1, salto
                                li a2, 1
                                li a0, 1 
                                li a7, 64 
                                ecall\n'''
            
        elif isinstance(instr.cad[0], ExpresionNumero):
            
            exp=resolver_expresion_aritmetica(instr.cad[0], ts)
            
            ts.salida += f'''mv a0, {exp}
                            li a7, 1
                            ecall\n'''


            
        elif len(instr.cad) == 1:
           
            #ts.salida += f'''-----------------llegaste-----------------{type(instr.cad[0])}\n'''
            if isinstance(instr.cad[0], ExpresionAccesoArray):
                
                #ts.salida += f'''acceso vector{(instr.cad[0].acceso)}\n'''
                id=instr.cad[0].id
                temp1 = ts.generateTemporal()
                temp2 = ts.generateTemporal()
                temp3 = ts.generateTemporal()
                temp4= ts.generateTemporal()
                desplazamiento=instr.cad[0].acceso.val*4
               
                ts.salida += f'''la {temp1},{id}\n'''
                ts.salida += f'''li {temp2},{desplazamiento}\n'''

                ts.salida += f'''add {temp1},{temp1},{temp2}\n'''
                ts.salida += f'''lw {temp3},0({temp1})\n'''

                ts.salida += f'''mv a0, {temp3}\n'''
                ts.salida += f'''li a7, 1\n'''
                ts.salida += f'''ecall\n'''

                ts.salida += f'''la a1, salto
                                    li a2, 1
                                    li a0, 1 
                                    li a7, 64 
                                    ecall\n'''  
                # exp=resolver_expresion(instr.cad[0].acceso, ts)
                # ts.salida += f'''mul {temp2},{exp},temp4 #Calcular el desplazamiento ({exp} * 4)\n'''
              
                # ts.salida += f'''add {temp1},{temp1},{temp2}\n'''

                # ts.salida += f'''lw {temp3},0({temp1})\n'''  

                # ts.salida += f'''mv {temp3}, {temp1}\n'''
                # ts.salida += f'''li a7, 1\n'''
                # ts.salida += f'''ecall\n'''


            else:
                ts.salida += f'''no es acceso vector\n'''






