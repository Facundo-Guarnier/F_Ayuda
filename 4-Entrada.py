print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")
print ("---------------------------------------------------------------")
print ("----------------------Entrada/Input----------------------------")   #Metodos para que el usuario ingrese un numero o letras.
                                                                            #Están escritos como anotacion para acelerar el proceso de los otros temas.

entero = int(input("Ingrese un numero entero: "))                           #Solo deja ingresar números entero.

nombre1 = str(input("Cual es tu nombre: "))                                 #Deja ingresar letras y números.

decimal1 = float(input("Ingrese un numero decimal"))                        #Números decimales (hay que utilizar el punto para el decimal).

absoluto1 = abs(float(input("Ingrese un numero para hacerlo absoluto: ")))  #Obtengo un numero en valor absoluto.

redondeo1= round(float(input("Ingrese un numero a redondear: ")))           #Redonde los números


print("\n------- Controlar si el formato ingresado es correcto --------")

edad = input("Ingrese su edad: ")

try: 
    edad = int(edad)
except:
    edad = False

if edad == False:
    print("No se ingreso una cadena de caracteres correcta (letras o simbolos)")
else:
    print("Tu edad es", edad, "año/s.")

print("\n+++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++\n")