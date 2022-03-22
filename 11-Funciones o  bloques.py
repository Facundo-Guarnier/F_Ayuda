print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

print("   def nombre_función(nombre_parametro1, nombre_paramento2, ...):  ")    #Definir función con sus lineas de código.
print("   nombre_función(valor_parametro1, valor_parametro2, ...)   ")          #Llamado de función.

entrada, entrada2 = 5, 6
#entrada = int(input("Introduzca un numero: "))
#entrada2 = int(input("Introduzca un numero: "))


print("------------No devuelve un valor------------")

def mi_función(a, b):                               #Se define la función con dos paramentos.
    suma = a + b
    resta = a - b
    multiplicación = a * b
    print(suma, resta, multiplicación)


mi_función(entrada, entrada2)                       #Se llama a la función.


print("------------Si devuelve un valor------------")

def mi_función(a, b):                               #Se define la función con dos paramentos.
    suma = a + b
    resta = a - b
    multiplicación = a * b
    return(suma, resta, multiplicación)             #Me devuelve un valor.


print(mi_función(entrada, entrada2))                #Imprimo directamente el valor.

resultado = mi_función(entrada, entrada2)           #O bien se lo asigno a una variable.
print(resultado)


print("-----------Solo variables locales----------")

def mi_función_2():                                #Se utilizan solo bariables locales, no se relaciona con el resto del programa.
    j = 8
    i = 2
    print(j + i)

mi_función_2()

print("--------Distinto orden de asignación--------")

def mi_función_3(c, d):                             #Asigno a la variable local 1 el valor de la variable global 2 y viceversa.
    print(c - d)

mi_función_3(d = 1000, c = 90)

print("--------------Predefinir valor--------------")

def mi_función_4(c = 0, d = 1):                     #Se puede dar una valor por defecto para cuando no tenemos un valor 
    print(c - d)                                    #para definir inicialmente con una variable global.

mi_función_4()                                      #Asignar por defecto.
mi_función_4(5, 10)                                 #Reasignar un nuevo valor.

print("--------Predefinir con una constante--------")

numero_1 = 1000                                     #Se puede predefinir una variable global a una variable local.

def mi_función_5(c = numero_1, d = 90):
    print(c - d)

mi_función_5()
mi_función_5(100, 100)

print("---------------Recursividad-----------------")   #Es una función que se llama a si misma, utilizando la condición base.
                                                        #Sin una base queda en un bucle infinito. Si se cumple la base devuelve un valor.
                                                        #Es como una pila de tareas, las de abajo espera a que se finalice la de arriba.

print("\n-----------Ejemplo 1-----------")
numero = 5

def f_factorial(n):
    if n == 1:
        return 1                                    #Base, 1! = 1
    else:
        print(n-1)
        return n * f_factorial(n-1)                 #Vuelve a llamar a la función. Hace todo un siclo sin números, por decir, hasta que llega a la base
                                                    #donde me dice que es 1 (return) y empieza al volverse, por decir.
                                                    #Es como el meme de los ladrillos en domino, hasta que no cae el ultimo los otros no se alinean.
                                                    #https://www.youtube.com/watch?v=qla3RXaRPCg

print(f_factorial(numero))

print("\n-----------Ejemplo 2-----------")

casas_para_regalo = ["Pepe", "Juan", "José", "Pedro", "Luis"]   
"""
    Se reparten casas a los elfos, si un elfo tiene mas de una casa se las puede repartir a
    a otros hasta que lleguen a 1. Donde este ultimo tiene que ir a la casa.
    Este caso se puede ver como la estafa piramidal, el de arriba se reparte todo el costo al de abajo.
"""

def envió_regalos(casas_para_regalo):
    if len(casas_para_regalo) == 1:                         #Base
        casas_para_regalo = casas_para_regalo[0]
        print("Se entrega a la casa", casas_para_regalo)
    else:
        mitad = len(casas_para_regalo) // 2
        mitad1 = casas_para_regalo[ :mitad]
        mitad2 = casas_para_regalo[mitad :]
        print(mitad1)
        print(mitad2)
        envió_regalos(mitad1)
        envió_regalos(mitad2)
 
envió_regalos(casas_para_regalo)                            #Se podría ver como agregar el numero de elfos correspondientes

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")