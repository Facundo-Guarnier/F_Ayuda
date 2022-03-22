"""
> Opcion (-a)
> Argemuneto (-a lalala)
  El argumento en lalala de la opcion -a


Ejercicio 1 - Getopt
    Crear una calculadora, donde se pase como argumentos luego de la opción -o el operador que se va a ejecutar (+,-,*,/), luego 
    de -n el primer número de la operación, y de -m el segundo número.

    Ejemplo:
    python3 calc.py -o + -n 5 -m 6
    5 + 6 = 11
    Considerar que el usuario puede ingresar los argumentos en cualquier orden. El programa deberá verificar que los argumentos 
    sean válidos (no repetidos, números enteros, y operaciones válidas.

"""
import sys
import getopt

numero1=""
numero2=""
operador=""
try:
    opcion, argumento = getopt.getopt(sys.argv[1:], "-o:-n:-m:")
    for opc, arg in opcion:
        if opc == "-o" :
            if arg in "- + / *" and operador == "":
                operador = arg
            else:
                print("Error: Operador no valido o repetido.")
                exit()
        elif opc == "-n":
            if numero1 == "": 
                numero1 = int(arg)
            else:
                print("Error: Operador repetido.")
                exit()
        elif opc == "-m":
            if  numero2 == "":
                numero2 = int(arg)
            else:
                print("Error: Operador repetido.")
                exit()

    if operador == "+":
        print(numero1, "+", numero2, "=", numero1 + numero2)
    elif  operador == "-":
        print(numero1, "-", numero2, "=", numero1 - numero2)
    elif  operador == "/":
        print(numero1, "/", numero2, "=", numero1 / numero2)
    elif  operador == "*":
        print(numero1, "*", numero2, "=", numero1 * numero2)


except getopt.GetoptError as e:
    print("Error:", e)
    exit()

except ValueError as e:
    print("Error:", e)
    exit()



"""
Ejercicio 2 - Argparse
    Escribir un programa que reciba dos nombres de archivos por línea de órdenes utilizando los 
    parámetros “-i” y “-o” procesados con argparse.

    El programa debe verificar que el archivo pasado a “-i” exista en el disco. De ser así, lo 
    abrirá en modo de solo lectura, leerá su contenido, y copiará dicho contenido en un archivo 
    nuevo cuyo nombre será el pasado a “-o”. Si el archivo nuevo ya existe, deberá sobreescribirlo.

    Ejemplo:
    python3 copiar.py -i existente.txt -o nuevo.txt

"""
import argparse
import sys
from ast import arg

parse = argparse.ArgumentParser()
parse.add_argument("-i", type=str)      #Hay que hacer un add por cada opcion.
parse.add_argument("-o", type=str)
args=parse.parse_args()

with open(args.i, 'r') as archivo1:
    mensaje = archivo1.read()
    with open(args.o, 'w') as archivo2:
        archivo2.write(mensaje)         #Si el archivo no existe, es creado.

# "archivo1.close()"" no es necesaria por la utilizacion del "with open...""

print("El archovo", args.i, "se copió a", args.o)