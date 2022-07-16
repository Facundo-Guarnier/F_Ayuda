'''
 - Permiten almacenar valores de distinto tipo e incluso listas y otros diccionarios
 - los valores almacenador se asocian a una clave en forma clave:valor
 - dichos elementos no estan ordenados
'''

romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}    #* Ejemplo de diccionario con claves/valores

romans['D'] = 500                                        #* Se adicionan elementos al diccionario
romans['M'] = 1000

romans.values()                                          #* Muestra los valores (values)

romans.keys()                                            #* Muestra las llaves (keys)

romans['X']                                              #* Accedo al valor de la clave X 
print(romans['X']) 

del romans['X']                                          #* Se elimina un elemento de el diccionario

dict_1 = {'a' : 1, 'b' : 2, 'c' : 3 , 'd' : 4}           #* Recibe como parámetro otro diccionario. Si se tienen claves iguales, actualiza el valor de la clave repetida;
dict_2 = {'c' : 6, 'b' : 5, 'e' : 9 , 'f' : 10}          #* si no hay claves iguales, este par clave-valor es agregado al diccionario.
dict_1.update(dict_2)
print(dict_1)

#! A un diccionario se le pueden agregar tuplas o listas tambien

for key in romans:                                       #* Recorrer un diccionario
  print (key, ":", romans[key])

for i in romans.keys():                                  #* Recorrer valores de un diccionario
  print (romans[i])