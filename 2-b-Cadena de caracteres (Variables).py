print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")
print ("---------------------------------------------------------------")
print ("------------------- Cadena de caracteres ----------------------\n") 

#Una variable str se puede usar como una lista. Ver su longitud y cada elemento.

a = "uno-"
b = "/dos"
print(a + b)                        #Operación suma, concatena las cadenas (es distinto que poner ,).
print(a * 4)                        #Repite las palabras la cantidad de veces.


print("-----------------")


nombre = "Jorge"
indice = 0
while indice < len (nombre):         #Imprimir cada caracter.
    letra = nombre [indice]
    print(letra)
    indice += 1

print()

for letra in nombre:                #Imprimir cada caracter.
    print(letra)

frase = "esto se separa"
lista_nueva = frase.split()         #Separa una cadena de caracter en una lista (cada palabra es un elemento de la lista).

print("-----------------")


nombre = "Facundo"              
recorte = nombre[: 3]               #Indices de los elementos.
print(recorte)
recorte = nombre [2: 4]
print(recorte)


print("-----------------")


nombre = "Facundo"                  #Busqueda de elementos dentro de la variable.
busqueda = "Fa" in nombre
print(busqueda)


print("-----------------")


nombre1 = "aaa facundo"                             #> o <, es para comparar la primera letra y saber cual esta 
nombre2 = "aaa Jorge"                               #primera en el abecedario, si son iguales pasa a la segunda y etc.
                                                    #Primero están las letras en mayúsculas.

if nombre1 < nombre2:
    print(nombre1, "no deberías leer esto, la J esta en mayúsculas")
else:
    print(nombre2, " esta antes por la mayúscula")


print("\n++++++++++++++++++++++++++++++++++++++ FIN ++++++++++++++++++++++++++++++++++++++++++++++++++")
