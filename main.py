
#from analizador.procesos import *
import analizador.analizador as g

from procesos.procesar_instrucciones import procesar_instrucciones


from tabla.tablaSimbolos import TablaSimbolos




if __name__ == '__main__':

    input_text ='''

        function saludo():string{
            return "Hola Mundo";
        }

        console.log(saludo());
    '''
    
    instrucciones = g.parse(input_text)
    ts = TablaSimbolos()
    try:
        procesar_instrucciones(instrucciones, ts, save=True)
        procesar_instrucciones(instrucciones,ts)
    except Exception as e:
        print("Error", e)
        
    print(ts.salida)

    

    # recorrer ts
    print('Tabla de simbolos:')
    for simbolo in ts.simbolos.values():
        print(simbolo.id, simbolo.tipo, simbolo.valor)


    print("-----------------Errores-----------------")
    print(ts.errores)
        
    
   


'''
                console.log("--------------------------");
                console.log("----ARCHIVO INTERMEDIO----");
                console.log("----------15 pts----------");
                console.log("--------------------------");

                console.log("");
                console.log("=======================================================================");
                console.log("=============================IFs ANIDADOS==============================");
                console.log("=======================================================================");
                var a: number = 909;
                var aux: number = 10;
                if (aux > 0) {
                    console.log("PRIMER IF CORRECTO");
                    if (true && (aux == 1)) {
                        console.log("SEGUNDO IF INCORRECTO");
                    } else if (aux > 10) {
                        console.log("SEGUNDO IF INCORRECTO");
                    } else {
                        console.log("SEGUNDO IF CORRECTO");
                    }
                } else if (aux <= 3) {
                    console.log("PRIMER IF INCORRECTO");
                    if (true && (aux == 1)) {
                        console.log("SEGUNDO IF INCORRECTO");
                    } else if (aux > 10) {
                        console.log("SEGUNDO IF INCORRECTO");
                    } else {
                        console.log("SEGUNDO IF CORRECTO");
                    }
                } else if (aux == a) {
                    console.log("PRIMER IF INCORRECTO");
                    if (true && (aux == 1)) {
                        console.log("SEGUNDO IF INCORRECTO");
                    } else if (aux > 10) {
                        console.log("SEGUNDO IF INCORRECTO");
                    } else {
                        console.log("SEGUNDO IF CORRECTO");
                    }
                }

                for (var i: number = 0; i <= 9; i++) {
                    var output: string = "";
                    for (var j: number = 0; j <= (10 - i); j++) {
                        output = output + " ";
                    }
                    for (var k: number = 0; k <= i; k++) {
                        output = output + "* ";
                    }
                    console.log(output);
                }



'''



'''
                console.log("----------------------");
                console.log("----ARCHIVO BASICO----");
                console.log("--------16 pts--------");
                console.log("----------------------");

                var bol: boolean = false;
                var bol2: boolean = !bol;
                var cad1: string = "imprimir";
                var cad2: string = "cadena valida";

                var val1: number = 7 - (5 + 10 * (2 + 4 * (5 + 2 * 3)) - 8 * 3 * 3) + 50 * (6 * 2);
                var val2: number = (2 * 2 * 2 * 2) - 9 - (8 - 6 + (3 * 3 - 6 * 5 - 7 - (9 + 7 * 7 * 7) + 10) - 5) + 8 - (6 - 5 * (2 * 3));
                var val3: number = val1 + ((2 + val2 * 3) + 1 - ((2 * 2 * 2) - 2) * 2) - 2;

                console.log("El valor de val1 es:", val1);
                console.log("El valor de val2 es:", val2);
                console.log("El valor de val3 es:", val3);
                console.log("El resultado de la operación es:", val3);
                console.log("El valor de bol es:", bol);
                console.log("El valor de cad1 es:", cad1);
                console.log("El valor de cad2 es:", cad2);
                console.log("El valor de bol2:", bol2);

                var a: number = 100;
                var b: number = 100;
                var c: number = 7;
                var f: boolean = true;
                var j: number = 10;
                var k: number = 10;

                console.log((a > b || b < c));

                console.log((a == b && j == k) || 14 != c);

                var val: number = 5;
                var resp: number = 5;
                var valorVerdadero: number = 100;

                console.log((valorVerdadero == (50 + 50 + (val - val))) && (!(!true)));

                var x1: number = 15;
                console.log(x1 % 2 == 0);

                 for (var i: number = 0; i <= 9; i++) {
                    var output: string = "";
                    for (var j: number = 0; j <= (10 - i); j++) {
                        output = output + " ";
                    }
                    for (var k: number = 0; k <= i; k++) {
                        output = output + "* ";
                    }
                    console.log(output);
                }
'''


'''

            console.log("--------------------------");
            console.log("---------ARREGLOS---------");
            console.log("----------12 pts----------");
            console.log("--------------------------");

            console.log("");
            console.log("=============================================");
            console.log("================CREACIÓN=====================");
            console.log("=============================================");
            var arr1: number[] = [8, 4, 6, 2];
            var arr2: number[] = [40, 21, 1, 3, 14, 4];
            var arr3: number[] = [90, 3, 40, 10, 8, 5];
            console.log("Se crean los arreglos arr1, arr2, arr3");
            console.log("arr1: ", arr1);
            console.log("arr2: ", arr2);
            console.log("arr3: ", arr3);

            console.log("");
            console.log("=============================================");
            console.log("=================ACCESO======================");
            console.log("=============================================");

            console.log("arr1: ", arr1[1]+4);
            console.log("arr2: ", 5+8*5-arr2[2]);
            console.log("arr3: ", arr3[4]*8);

            console.log("=============================================");
            console.log("================FUNCIONES====================");
            console.log("=============================================");

            console.log("============ PUSH");
            console.log("arr1: ", arr1);
            arr1.push(9);
            console.log("arr1: ", arr1);

            console.log("============ POP");
            console.log("arr2: ", arr2);
            console.log("pop arr2: ", arr2.pop());
            console.log("arr2: ", arr2);

            console.log("============ INDEXOF");
            console.log("Posición 3: ", arr3.indexOf(10));
            console.log("Posición -1: ", arr3.indexOf(666));

            console.log("============ JOIN");
            console.log("arr1: ", arr1.join());
            console.log("arr2: ", arr2.join());
            console.log("arr3: ", arr3.join());

            console.log("============ LENGTH");
            console.log("arr1: ", arr1, "length: ", arr1.length);
            console.log("arr2: ", arr2, "length: ", arr2.length);
            console.log("arr3: ", arr3, "length: ", arr3.length);
            console.log("Eliminando indices: ", arr1.pop(), arr2.pop(), arr3.pop());
            console.log("arr1: ", arr1, "length: ", arr1.length);
            console.log("arr2: ", arr2, "length: ", arr2.length);
            console.log("arr3: ", arr3, "length: ", arr3.length);

    '''

