print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("---------------------------------------------------------------")
print("-------------------------Listas--------------------------------")

mi_lista = [00, 11, 22, 33, 44 , 5555]      #Una lista de toda la vida, se arma con corchetes.

print(len(mi_lista))                #Longitud de la lista.
print(mi_lista)                     #Imprime la lista completa.
print(mi_lista[2])                  #Muestra el tercer elemento de la lista ya que empieza con el 0.
print(mi_lista[1:5:1])              #Imprime del elemeto 1 al 4.
print(mi_lista[-1::])               #Imprime el ultimo.

print("------Modificar------")

mi_lista2 = mi_lista.copy()
print("Lista 2:", mi_lista2)    #El beneficio de copiar es que se puede modificar una y la 
                                #otra permanece igual.

mi_lista.append(66)             #Agregue un elemento al final de la lista.
print(mi_lista)

mi_lista += [99999]             #Agregar un nuevo elemento al final (entre corchetes si o si)

l1 = ["a", "b"]                 
l2 = ["c", "d"]
print(l1 + l2)                  #Une las listas, no suma elementos.
l1.extend(l2)                   #Dos listas concatenadas.
print(l1)
print(l2 * 3)                   #Repite 3 veces la lista pero en una sola lista.

mi_lista.insert(5, 55)          #Inserta un nuevo elemento en el inicie 5 en este caso (no reemplaza).
print(mi_lista)                 #Si el indice no existía se agrega al final.

mi_lista[4] = 4444              #Remplaza el valor 4.
print(mi_lista[4])


print(mi_lista.pop(5))          #Corta el indice 5 de la lista y se le puede asignar a una variable. 
print(mi_lista)                 #Modifica la lista y puedo asignar el valor.

mi_lista.remove(11)             #Remueve el elemento 11, el indice.
print(mi_lista)

"""
del mi_lista[1 : 5]             #Elimina los elementos del 1 al 4.
"""

mi_lista.sort()                 #Ordena la lista ascendentemente según el valor del elemento no por indice,
print(mi_lista)                 #solo con mismos elementos (str o int, no los dos). 
                                #Orden: numero > mayúsculas > minúsculas

mi_lista.sort(reverse=True)     #Ordena la lista descendentemente según el valor del elemento no por indice, 
print(mi_lista)                 #solo con mismos elementos (str o int, no los dos). 

print(set(mi_lista))            #Limpia los elementos repetidos pero los desordena. Se transforma en un conjunto
                                #Para tener otra vez la lista: mi_lista = list(set(mi_lista))

frase = "estosesepara"
print(frase.split())            #Separa una cadena de caracter en una lista (cada palabra es un elemento de la lista)

print("------Busqueda------")

print(11 in mi_lista)           #Busca el elemento y me devuelve verdadero/falso.

print(mi_lista.index(22))       #Devuelve el indice del elemento (solo muestra el primer valor encontrado).

print(mi_lista.count(00))       #Contar elementos.

print("Mayor elemento", max(mi_lista))          #Máximo.
print("Menor elemento", min(mi_lista))          #Minio.
print("Suma los elemento", sum(mi_lista))       #Suma los elementos, solo con int.

print("-------Extra--------")

"""mi_lista[10] = "Este elemento no existía, no se puede agregar" """ #NO se puede agregar un elemento a un indice que NO existe.

mi_tupla = tuple(mi_lista)      #Convertir la lista en tupla.
print(mi_tupla)

for i in range(len(mi_lista)):  #Imprime cada elemento suelto.
    print(mi_lista[i])

for i in mi_lista:              #Imprime cada elemento suelto.
    print(i)


mi_lista.clear()                #Borra toda la lista.
print(mi_lista)



print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")