print()
print("+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++")
print()
print ("---------------------------------------------------------------")
print ("---------------------------Print-------------------------------")  

print ("Hola kpo el primer código de verdad que hago, vamos a ver si funciona")
print ("Si funciono lpm ggggggggg pero vos no lo viste xd, nos vimos en diznei")

print("Renglón 1 \nRenglón 2")              #Baja de renglón lo que esta despues del "\n", se escribe con AltGr + ?.

variable_ejemplo = "18"
print ("Mi edad es: " + variable_ejemplo)   #No puedo usar print con el conector "+" si las variables no numéricas (int) pero si con letras y números (str).
                                            #Para usar una variable numérica se puede usar ",".
                                            #Porque con el + la pc piensa que quiero sumar y no unir palabras.
                                    
print("hola,", end=" ")                     #Remplaza el ultimo valor de print (por default es \n).
print("adiós pero separado")

print("hola,", end="")
print("adiós pero pegado")

print("El me dijo: \"Hola kpo, ¿Que haces?\"")      #Para usar algún símbolo en print se usa " \ ".
print("El me dijo: 'Hola kpo, ¿Que haces?'")        #También se puede usar diéresis.

print()
print("---------------------------------------------------------------")
print("--------------------------Variable-----------------------------")   #Tiene un valor numérico o en letra.
                                                                           #Para renombrar la variable y todos sus llamados se usa "ctrl + F12".
                                                                           #Todo con minúscula y separado con guion bajo.

variable_1 = 8 + 5          #Una variable con una suma.
print(variable_1 + 100,)    #Realiza una suma de la variable + 100
print(variable_1, 100)      #Une la variable con el 100

print()
print ("---------------------------------------------------------------")
print ("------------------------Constante------------------------------") #Una vez definida no se puede cambiar.
                                                                          #Se escribe todo con mayúsculas y guion bajo.

MI_CONSTANTE = 3.14159
print(MI_CONSTANTE)

print()
print ("---------------------------------------------------------------")
print ("----------------------Entrada/Input----------------------------")   #Metodos para que el usuario ingrese un numero o letras.
                                                                            #Están escritos como anotacion para acelerar el proceso de los otros temas.

"""int(input("Ingrese su edad:"))                                      #Solo deja ingresar números entero.
str(input("Cual es tu nombre"))                                     #Deja ingresar letras y números.
float(input("Ingrese un numero decimal"))                           #Números decimales (hay que utilizar el punto para el decimal).
abs(float(input("Ingrese un numero para hacerlo absoluto: ")))      #Obtengo un numero en valor absoluto.a =
round(float(input("Ingrese un numero a redondear: ")))              #Redonde los números

edad = int(input("Ingrese su edad:"))        #Al establecer una variable adelante es darle el valor de lo que se ingresa.
print(edad)"""

print()
print("---------------------------------------------------------------")
print("-------------------- Tupla/Tuple (...) ------------------------")    #https://www.youtube.com/watch?v=PjCBukZttG4
                                                                            #Es una lista inmutable, ni agregar ni modificar.

mi_tupla = ("lpm", 5.0, "gg", "ahora funciona", "88,9", 55, "lpm") #Se arma con parentesis, va del 0 al infinito, se separa con comas y se llama con [].

print(len(mi_tupla))    #Longitud de la tupla.

print()

print(mi_tupla [1:4])   #Muestro los elementos del 1 al 4.
print(mi_tupla [5])     #Muestro solo el elemento 5.
print(mi_tupla)         #muestra todos los elementos de la tupla.
print(mi_tupla[-2])     #Muestra el penúltimo valor. Con los negativos empiezo de atrás para adelante desde el -1. 

print()

print(55 in mi_tupla)                       #Busca el elemento y me devuelve verdadero/falso.
print(mi_tupla.index("ahora funciona"))     #Devuelve el indice del elemento (solo muestra el primer valor encontrado).
print(mi_tupla.count("lpm"))                #Cuenta cuantas veces esta el elemento.

print()
print("---------------------------------------------------------------")
print("-------------------------Listas--------------------------------")

mi_lista = [00, 11, 22, 33, 44 , "no se que onda"]      #Una lista de toda la vida, se arma con corchetes.

print(len(mi_lista))                #Longitud de la lista.
print(mi_lista)                     #Imprime la lista completa.
print(mi_lista[2])                  #Muestra el tercer elemento de la lista ya que empieza con el 0.
print(mi_lista[1:5])                #imprime del elemeto 1 al 4.

print()

mi_lista.append(66)     #Agregue un elemento a l final d la lista.
print(mi_lista)
mi_lista[4] = 4444      #Remplaza el valor 4.
print(mi_lista[4])

print()

ultimo = mi_lista.pop()         #Corta el ultimo elemento a la lista y se le puede asignar a una variable. 
print(mi_lista)
print("Corte el elemento", ultimo)

print()

print(11 in mi_lista)           #Busca el elemento y me devuelve verdadero/falso.
print(mi_lista.index(22))       #Devuelve el indice del elemento (solo muestra el primer valor encontrado).
print(mi_lista.count(00))       #Cuenta cuantas veces esta el elemento.

print()

"""mi_lista[6] = "Este elemento no existía, no se puede agregar" """ #NO se puede agregar un elemento a un indice que NO existe.

print()
print("---------------------------------------------------------------")
print("------------------------Diccionario----------------------------")    #https://www.youtube.com/watch?v=vAy4IM7NLIQ parte 1
                                                                            #https://www.youtube.com/watch?v=hjNWsqLAPv4&list=RDCMUC7QoKU6bj1QbXQuNIjan82Q&index=1 parte 2.

ejemplo = {"clave":"valor"}

mi_diccionario = {"rojo":"FF0000", "azul":"color", "facu":[18, "1,73"], "68":"numero"}      #Es como una lista pero con comparación incluida,
                                                                                            #"azul" en la clave para el valor "color", se separa con ":".
                                                                                            #No se puede repetir claves pero si el valor.
                                                                                            #Puede tener listas, tuplas o también otros diccionarios dentro.
print(mi_diccionario)

print(mi_diccionario["rojo"])                   #Muestra el valor de la clave

mi_diccionario["celeste"] = "color"             #Agregar un nuevo elemento.
print(mi_diccionario)

mi_diccionario["azul"] = "¿color o numero?"     #Cambiar el valor a una clave.
print(mi_diccionario)

del(mi_diccionario["azul"])                     #Elimina el conjunto/par utilizando la clave.
print(mi_diccionario)

print()

print(mi_diccionario.get("amarillo", "El color amarillo no esta en el diccionario"))     #Busca la clave pero si no existe muestra el sino.
print("azul" in mi_diccionario)             #Comprueba su la clave existe, devuelve verdadero o falso.

print()

print(mi_diccionario.keys())                #Impreme las claves solamente.
print(mi_diccionario.values())              #Impreme los valores solamente.
print(mi_diccionario.items())               #Impreme los pares es tuplas para usarlos en listas.

print()

print(len(mi_diccionario))                  #Cantidad de claves.
mi_diccionario.clear()                      #Borra todo el diccionario.
print(mi_diccionario)

print("---------------------------------------------------------------")
print("--------------------Símbolos: Matematicos----------------------")

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
print("PAra ejecutar una celda separada se usa: " + celda)


print()
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print()
print("---------------------------------------------------------------")
print("--------------------- Control de flujo ------------------------")
print("---------------------------------------------------------------")
print()

print("---------------------------------------------------------------")
print("------------------- Condicional (if, else) --------------------")    #El código a ejecutar dentro de los condicionales tiene que estar con indentation.

la_condición = 15

if (la_condición > 15) and (la_condición < 100):                        #"si", si no cumple no hace nada.
     print("No deberia leer esto ya que no se cumple la condición1")

elif (1 < la_condición < 10):
     print("No deberia leer esto ya que no se cumple la condición2")

elif (la_condición == 15):                                            #Si el "si" anterior no se cumple pasa a este nuevo "si" ya que tiene condición.
     print("Es correcto")

else :                                                                #"Sino", cuando ningún "si" se cumplió, no tiene condición.
     print("No deberia leer esto ya que no se cumple la condición3")
     pass                                                             #Es para un Condicional cuando no se le asigna una acción y evitar error.

print()
print("---------------------------------------------------------------")
print("--------------------Control Repetitivas------------------------")
print()

repetir_while = "while" #Es un Si esto es vedadero repito esto otro. Mientras que...
print("Para repetir un bloque mientras la condición es verdadera se utiliza: " + repetir_while + "\nsi queres que se repita hasta que la respuesta es correcta se pone u not adelante de la condición")

while True:           #Esto genera un bucle infinito.
     print("Hola")    
     break            #Esto termina el bucle completo, con los posibles else (sino:)
else:       #Funciona igual que el else del if, también se usa para for
     print("Aca nunca llega por el break, ne deberías leer esto") 

variable_2 = 0

"""while variable_2 < 6: 
     variable_2 += 1
     if (variable_2 == 3):
          continue            #Cuando el programa llega hasta Continue, este vuelve al inicio del programa sin hacer lo que hay debajo
                              #Se utiliza con un "if" sino queda también en un bucle.
     print (variable_2)"""

repetir_for = "for"
print("Para repetir un bloque x cantidad de veces se utiliza: " + repetir_for)

range (1, 10, 5) #Desde, hasta, paso o de a cuanto (por defecto es 1), se separan con una coma, es como un contador (solo con valores enteros).
                 #Sirve para un bucle for con listas o tuplas. 

"""mi_tupla2 = ('rojo', 'verde', 'amarillo')
     for color in mi_tupla2:  #Esto es como un range, lo que esta antes de in es una nueva variable y 
          print(color)        #lo que esta despues es una cupla (solo con valores enteros)."""

print()
print("+++++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++")
print()

