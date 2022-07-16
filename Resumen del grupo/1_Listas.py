
#! Sugerencia: habilitar en Visual el plugin "BetterComments" para ver mejor algunas anotaciones especiales.

my_array = []
my_array.append (1)                            #* Se agregan elementos a la lista
my_array.append (2)
my_array.append (3)
my_array.append (4)

for i in my_array:
    print(i)

for i in range (0, len(my_array)):             #* Para recorrer la lista desde un punto en particular
    print(str(i) + ':' + str(my_array[i]))

for i in range (0, len(my_array), 2):          #* Para recorrer la lista desde un punto en particular, de 2 en 2
    print(str(i) + ':' + str(my_array[i]))

my_array[0]                                    #* Muestra el valor de indice 0
my_array[1::]                                  #* Muestra los valores a partir del indice 1
my_array[1:4:]                                 #* Muestras los valores desde 1 hasta 4
my_array[::-1]                                 #* Muestra la lista inversa
my_array[-1::]                                 #* Muestra el ultimo valor de la lista
my_array[1:4:2]                                #* Muestras los valores desde el indice 1 al 4 de 2 en 2

my_array.insert(3,2)                           #* Para agregar un elemento en un punto intermedio se usa insert, se agrega en el index 3, el valor 2

my_array.index(2)                              #* Devuelve el primer valor repetido de la lista

my_array.remove(3)                             #* Remueve un elemento determinadod de la lista
my_array.pop()                                 #* Para eliminar el ultimo elemento se usa pop