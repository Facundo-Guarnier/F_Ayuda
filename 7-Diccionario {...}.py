print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("---------------------------------------------------------------")
print("------------------------Diccionario----------------------------")    #https://www.youtube.com/watch?v=vAy4IM7NLIQ parte 1
                                                                            #https://www.youtube.com/watch?v=hjNWsqLAPv4&list=RDCMUC7QoKU6bj1QbXQuNIjan82Q&index=1 parte 2.


ejemplo = {"clave1":"valor 1", "clave2":"valor1 o 2"}

mi_diccionario = {"rojo":"FF0000", "azul":"color", "facu":[18, "1,73"], "68":"numero"}      #Es como una lista pero con comparación incluida,
                                                                                            #No se puede repetir claves pero si el valor.
                                                                                            #Puede tener listas, tuplas o también otros diccionarios dentro.
print(mi_diccionario)


print("-----Modificar-----")

mi_diccionario["celeste"] = "color"             #Agregar un nuevo elemento.
print(mi_diccionario)

mi_diccionario["azul"] = "¿color o numero?"     #Cambiar el valor a una clave.
print(mi_diccionario)

del(mi_diccionario["azul"])                     #Elimina el conjunto/par utilizando la clave.
print(mi_diccionario)

mi_diccionario.popitem()                        #Elimina el ultimo par.
print(mi_diccionario)

print("------Busqueda------")

print(mi_diccionario["rojo"])               #Devuelve el valor de la clave.

print(mi_diccionario.get("amarillo", "El color no esta en el diccionario"))     #Busca la clave y devuelve el valor, pero si no existe muestra el "sino".

print("azul" in mi_diccionario)             #Comprueba si la clave existe, devuelve verdadero o falso.

print(mi_diccionario.keys())                #Impreme las claves solamente.
print(mi_diccionario.values())              #Impreme los valores solamente.
print(mi_diccionario.items(), "+++++++++++++++++++++++++++++++")               #Impreme los pares de tuplas en listas.

print("-------Extra------")

print(len(mi_diccionario))                  #Cantidad de claves.

mi_diccionario.clear()                      #Borra todo el diccionario.


tupla_o_lista = (11, 22, 33, 44)            #Se puede asignar un valor desde una lista.

mi_diccionario2 = {tupla_o_lista[0]: "uno", tupla_o_lista[1]: "dos"}

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")