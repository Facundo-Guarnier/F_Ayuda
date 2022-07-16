
'''
Excepciones:

    Durante la ejecución de un programa, si dentro de una función surge una excepción y la función no la maneja, 
    la excepción se propaga hacia la función que la invocó, si esta otra tampoco la maneja, la excepción continua propagándose 
    hasta llegar a la función inicial del programa y si esta tampoco la maneja se interrumpe la ejecución del programa.

    El manejo de excepciones tomar acciones de recuperación para evitar la interrupción del programa o, al menos, para realizar 
    algunas acciones adicionales antes de interrumpir el programa.

    Los tipos comunes de errores son:

        - TypeError: aparece cuando una operación es realizada con una incorrecto o no soportado tipo de objeto. Por ejemplo:
            Cuando se usa un + para intentar unir un string y un valor int
        - ZeroDivisionError: aparece en una division por 0.
        - NameError: aparece cuando se trata de usar una variable no declarada anteriormente.
        - ValueError: aparece caundo el caracter introducido no es del valor esperado. Por ejemplo:
            Cuando se espera un valor numerico del tipo int y se ingresa un string.
'''

def division(n1,n2):                
    return n1/n2

'''
En la funcion de division anterior, si n2 fuera 0, python devolveria un error del tipo ZeroDivisionError.
Este error puede ser capturado para modificar la respuesta de python mediante try/except:
'''

def division (n1,n2):
    try:                                              #* De esta manera se prueba la condicion, y de dar error se devuelve un mensaje personalizado
        return n1/n2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operación errónea"


while True:
    try:
        num1 = int(input("Ingrese numero:"))
        num2 = int(input("Ingrese numero:"))
        break
    except ValueError:
        print("Los valores introducidos no son correctos. Intentalo de nuevo")
print(division(num1,num2))

'''
Lanzar excepciones: permite al programador forzar a que ocurra una excepción específica.
'''

def eval_edad(edad):
    if edad<0:
        raise TypeError("No se permiten edades negativas") 
    if edad<20:
        return "eres muy joven"
    elif edad<40:
        return "eres joven"
    elif edad<65:
        return "eres maduro"
    elif edad<100:
        return "Cuidate..."
print(eval_edad(10))

import math

def calraiz(n1):
    if n1<0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(n1)
op1 = int(input("Introducir numero: "))
print(calraiz(op1))
print("Programa terminado")