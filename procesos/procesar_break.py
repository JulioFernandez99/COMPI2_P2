def procesar_break(instr,ts):
    ts.salida+=f'''j {ts.pop_break()}\n'''