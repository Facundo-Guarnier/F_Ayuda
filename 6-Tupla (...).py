print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

print("---------------------------------------------------------------")
print("-------------------- Tupla/Tuple (...) ------------------------")    #https://www.youtube.com/watch?v=PjCBukZttG4
                                                                            #Es una lista inmutable, ni agregar ni modificar.

mi_tupla = (00, 11, 22, 33, 44, 55)     #Se arma con parentesis (...).
tupla_unitaria = (99999,)               #Tupla unitaria.


print(mi_tupla [1:4])   #Muestro los elementos del 1 al 4.
print(mi_tupla [5])     #Muestro solo el elemento 5.
print(mi_tupla[-2])     #Muestra el penúltimo valor. Con los negativos empiezo de atrás para adelante desde el -1. 

print("------Busqueda------")

print(55 in mi_tupla)           #Busca el elemento y me devuelve verdadero/falso.
print(mi_tupla.index(44))       #Devuelve el indice del elemento (solo muestra el primer valor encontrado).
print(mi_tupla.count(66))       #Cuenta cuantas veces esta el elemento.

print(max(mi_tupla))        #Máximo
print(min(mi_tupla))        #Mínimos

print("---Desempaquetado---")

mi_tupla2 = ("Facu", 18, "febrero", 2002, "18 años")    #Se le asigna cada valor
nombre, dia, mes, años, edad = mi_tupla2                #Si o si con todos los indices, ni mas ni menos.

print("--------Extra-------")

mi_lista = list(mi_tupla)               #Convertir la tupla en lista.
print(mi_lista)

for i in range(len(mi_tupla)):          #Imprime cada elemento suelto.
    print(i)

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")