print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("---------------------------------------------------------------")
print("---------------------------For/Por-----------------------------")

print("For variable_nueva in condición:")

print("range(x, y, z)")



print("---------Variable----------")

i = 5
for variable in range(i):                                       #Variable, con una tal cantidad.
    print(variable)

print("---------Rango----------")

for variable in range(1, 5, 1):                                 #Range (desde, hasta, de a cuanto) El 5 no se cuenta
    print(variable)

print("--------Palabra---------")

for variable in "Jorge":                                        #Palabras, recorre cada caracter.
    print(variable)

print("------Lista/Tupla-------")

lista = [5, 3, 8, 9, 1]                                         #Tuplas o listas, recorre cada elemento.
for variable in lista:
    print(variable)

print("------Diccionario------")

diccionario = {"hola": "palabra", 15: "numero", 8: "numero"}    #Diccionario, recorre las claves y/o los valores, depende que pones .keys etc.
for clave, valor in diccionario.items():
    print(clave, valor)

print("---------Extra---------")

for variable in range(0, 8):
    if variable == 2:                           
        continue                        #Vuelve al inicio sin hacer lo que queda.
    if variable == 5:
        break                           #Termina con todo el bucle.
    print(variable)



print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")