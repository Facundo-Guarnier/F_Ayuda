print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("---------------------------------------------------------------")
print("------------------------Archivos-------------------------------")

c = open("Aca va la direccion del archivo C:\\Users\\Casa\\Desktop\\... .py")     #La direccion con doble barra y luego el permiso.

print("------------Leer-------------")

c = open("Aca va la direccion del archivo C:\\Users\\Casa\\Desktop\\... .py", "r")    #Cada vez que quiero leer el archivo hay que 
                                                                                                #abrirlo otra vez.
print(c.read())                 #Leer archivo entero.
print(c.readline())             #Lee por linea (linea 1).
print(c.readline())             #linea 2 (y asi copiando el mismo codigo).


for x in c:                     #Lee por linea.
     print(x)


print("----------Permisos-----------")

r = "Read, leer."
a = "Append, agregar codigo al final."
w = "Write, modificacion total o creear uno nuevo."
x = "Crear un arichivo nuevo."


print("----------Escribir-----------")

c = open("Aca va la direccion del archivo C:\\Users\\Casa\\Desktop\\... .py", "a")

c.write("\nNueva linea agregada desde otro archivo")


print("-----------Cerrar------------")

c.close()


print("----Comprobar existencia-----")

import os 

os.path.exists("Aca va la direccion del archivo C:\\... .txt")      #Devuelve True o False


print("----------Eliminar-----------")

import os 

if os.path.exists("Aca va la direccion del archivo C:\\... .txt"):
    os.remove("Aca va la direccion del archivo C:\\... .txt")        #Elimina el archivo.
else:
    print("El archivo no existe por lo tanto no se puede eliminar.")


print("---------------------------------------------------------------")
print("------------------Carpetas/directorios-------------------------")

print("----------Eliminar-----------")

import os 

os.rmdir("Aca va la direccion de la carpeta C:\\...")               #Elimina carpeta

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")