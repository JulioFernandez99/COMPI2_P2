.data ;pruebas
result: .word 0       #Variable para almacenar
msg_suma: .asciz "La suma es: "

.text
.globl main
main:

#Declaracion de Variable

li t0, 25  #Primer valor
li t1, 5   #Segundo valor

#Suma
jal ra, suma
jal ra, console_log

#Exit
li a7, 10       #syscall para terminar ejecucion
ecall

suma:
    add t2, t0, t1  #Suma de 2 numeros
    la t6, result   #Cargar el valor de result
    sw t2, 0(t6)    #Almacenar en result 
    ret


console_log:
    li a0, 1 # a0: file descriptor = 1 (stdout)
    la a1, msg_suma # a1: ubicacion del mensaje para el buffer
    li a2, 14 # a2: tamaño del buffer (14 bytes)
    li a7, 64 # a7: syscall code (write = 64)
    ecall # invoca la llamada al sistema

    lw a0, result       #Cargar resultado a A0
    li a7, 1            #syscall para imprimir enteros 
    ecall

    li a0, 10           #Salto de linea
    li a7, 11           #syscall para imprimir caracter
    ecall

    ret