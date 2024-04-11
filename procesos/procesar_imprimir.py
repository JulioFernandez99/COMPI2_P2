#---------------------------------------IMPRIMIR--------------------------------------


from procesos.resolver_expresion import resolver_expresion

def procesar_imprimir(instr,ts):
    
    tempcad = ''

    val=None
    if len(instr.cad) > 1:  
        for i in range(len(instr.cad)):
            val=resolver_expresion(instr.cad[i], ts)
            tempcad += str(val)+ ' '   
            
    else:
        val=resolver_expresion(instr.cad[0], ts)
        tempcad = str(val)
       

    if val != "ERARA91" :#none
        #print('>> ',tempcad)
        ts.salida += '>> '+tempcad + '\n'
        
        
