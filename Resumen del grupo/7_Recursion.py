'''
Recursividad: se denomina llamada recursiva a aquellas funciones que en su algoritmo, hacen referencia sí misma

Las llamadas recursivas suelen ser muy útiles en casos muy puntuales, pero debido a su gran factibilidad de caer en iteraciones infinitas, 
deben extremarse las medidas preventivas adecuadas y, solo utilizarse cuando sea estrictamente necesario y no exista una forma alternativa viable, 
que resuelva el problema evitando la recursividad.
'''

def mi_rec(value):

    print('voy por el ' + str(value))
    return mi_rec(value - 1) + value

#! La funcion anterior mostrara un error luego de alcanzar el limite de recursiones permitidas por python, para alterar este valor:

import sys
sys.setrecursionlimit(10000)
print(mi_rec(10000))

'''
Otros ejemplos de recursividad:
'''

#TODO: Hacer el factorial de un numero por recursividad. Ej: 5! = 5*4*3*2*1 = 120

def factorial(num):

    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))

#TODO: Recorrer una lista en forma recursiva desde el indice 0.

def rec_lista(lista, index):

    if index < len(lista):
        print(lista[index])
        return rec_lista(lista, index + 1)

lista = [1,2,3,4,5]
rec_lista(lista, 0)

#TODO: Sumar los elementos de una lista con recursividad.

def sumar_lista(lista):

    if lista == []:
        return 0
    else:
        return lista[0] + sumar_lista(lista[1:])

lista = [1,2,3,4,5]
print(sumar_lista(lista))

#TODO: Crear una lista en forma recursiva con numeros enteros descendentes desde un numero dado hasta 0

def crear_lista(num):

    if num == 0:
        return [0]
    else:
        return [num] + crear_lista(num - 1)

print(crear_lista(5))