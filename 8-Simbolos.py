print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("---------------------------------------------------------------")
print("--------------------Símbolos: Matematicos----------------------")

resta = "-"                                                     #Se puede restar int, listas, conjuntos(set), etc. No sucede lo mismo con la suma.
print("Para restar se usa:", resta)                             #Si no se puede restar un elemento de la segunda lista no se pone directamente.

suma_de_conjuntos = "|"                                         #Suma conjuntos(son como listas pero sin repetir elementos).
print("Sumar conuntos que no se puede usar el '+' se usa:", suma_de_conjuntos)

intersección = "&"                                              #Lo que se repite en dos conjuntos
print("Lo que tiene en común dos conjuntos:", intersección)

modulo = "%"                                                    #Me muestra el resto de la division.
print("El modulo es: " + modulo)

exponente = "**"                                                #Exponente.
print("El exponente es: " + exponente)

division_entera = "//"                                          #Me redonde el numero, siempre al menor -> 5.999 = 5
print("La division entera es: " + division_entera)

incremento = "+="                                               #Suma una cantidad x a la misma variable.
print("Para sumar x cantidad se usa: " + incremento)            

decremento = "-="                                               #Resta una cantidad x a la misma variable.
print("Para restar x cantidad se usa: " + decremento)           

division_rápida = "/="                                          #Divide la variable por x, devuelve el resultado.
print("Divide la variable por un numero:", division_rápida)

multiplicación_rápida = "*="                                    #Multiplica la variable por x, devuelve el resultado.
print("Multiplica la variable por un numero:", multiplicación_rápida)


print("\n---------------------------------------------------------------")
print("---------------------Símbolos: Comparación----------------------")

igual_que = ("==")                                              #Compara si es el mismo valor.
print("para comparar si son iguales se usa: " + igual_que)

distinto_que = ("!=")                                           #Compara si no es el mismo valor.
print("Distinto que se usa: " + distinto_que)

mayor_igual_que = ">="                                          #Mayor/igual.
print("Comparar mayo/igual se usa:", mayor_igual_que)

menor_igual_que = "<="                                          #Menor/igual.
print("Comparar menor/igual se usa:", menor_igual_que)



print("\n---------------------------------------------------------------")
print("-----------------------Símbolos: Lógicos------------------------")

y = ("and")                                                     #En serie.
print ("Devuelve verdadero si ambos lados son ciertos: " + y) 

o = ("or")                                                      #En paralelo.
print("Devuelve verdadero si uno de los dos es verdadero: " + o)

negar = ("not")                                                 #Cambia de verdadero a falso o viceversa.
print("Para cambiar de verdadero a falso o viceversa: " + negar)



print("\n---------------------------------------------------------------")
print("-----------------------Símbolos: Extras-------------------------")

celda = ("#%%")                                                 #Para ejecutar una parte del código
print("Para ejecutar una celda separada se usa: " + celda)

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")