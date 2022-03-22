print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

frase = (input("Introduce una cadena de caracteres:"))

print("--------Solo con 'str'--------")

print("Letras:", frase.isalpha())                   #Letras solas sin espacios.

print("Alfanumérico:",frase.isalnum())              #Letras y números sin espacios.

print("Números:", frase.isnumeric())                #Números solos sin espacios (números de otros idiomas).

print("Dígitos:", frase.isdigit())                  #Dígitos solos sin espacios.

print("Decimales:", frase.isdecimal())              #Solo de caracter decimal, puede tener 0 decimales.

print("Minúsculas:", frase.islower())               #Solo minúscula (no importa si hay números o símbolos, pero si o si una letra)

print("Mayúsculas:", frase.isupper())               #Solo mayúsculas (no importa si hay números o símbolos, pero si o si una letra)

print("Espacios:", frase.isspace())                 #Solo espacios

print("Forma de titulo:", frase.istitle())          #Todas las palabras con Mayúscula la primera letra.



print("\n--------Con cualquier formato--------")

print("Formato de int:", isinstance(frase, int))    #Si es int.

print("Formato de str:", isinstance(frase, str))

print("Formato de float:", isinstance(frase, float))


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

print("\n+++++++++++++++++++++++++++++++++++++++ FIN ++++++++++++++++++++++++++++++++++++++++++++++++++\n")