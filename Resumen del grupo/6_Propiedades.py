'''
Encapsulamiento: hablamos de ocultar los datos de atributos o métodos, más específicamente de protegerlos para que solo puedan ser 
cambiados mediante “operaciones definidas” para ello. Esto nos asegura por ejemplo que “no podremos modificar un atributo si no es a 
través de un método que hallamos creado específicamente para ello” y aquí es donde nacen los famosos “Getter, Setter, Deleter”

Lo que sucede es que en otros lenguajes es común utilizar el encapsulamiento, pero en Python las propiedades y métodos privados no existen, 
por lo que son fácilmente sobreescribibles (lo que quiere decir que este tema es practicamente al pedo en python).
'''

#* Atributos protegidos

class usuario (object):
    def __init__(self, nombre, clave):
        self.nombre = nombre
        self._clave = clave
        
Usuario1 = usuario ("Roberto", "qwerty")
print (Usuario1.nombre, Usuario1._clave)

'''
Como ves el atributo clave esta precedido por un guión bajo, lo que indica que es un atributo protegido. Lo cual establece que solo puede ser accedido 
por esa clase y sus sub-clases, es decir, aquellas que hereden de la clase padre.
'''

#* Atributos privados

class usuario (object):
    def __init__(self, nombre, clave):
        self.nombre = nombre
        self.__clave = clave
        
Usuario1 = usuario ("Roberto", "qwerty")
print (Usuario1.nombre, Usuario1._usuario__clave)

'''
Como ves podemos acceder igualmente a un atributo por más que sea privado y modificarlo de la misma manera. Pero no es lo que se “considera correcto”. 
Por lo que para ello si deseamos implementar métodos que nos permitan modificar estos atributos de la forma que se suele hacer en otros lenguajes donde 
se aplica “encapsulamiento” podemos hacerlo utilizando Getter, Setter, Deleter mediante el uso del decorador @Property.

Las propiedades nos permiten por ejemplo llamar código personalizado cuando un atributo, método, variable es mostrado/a, modificado/a, borrado/a.
'''

#* @Property

'''
La función integrada @property nos permitirá interceptar la escritura, lectura, borrado de los atributos y ademas nos permiten incorporar una documentación 
sobre los mismos.
Si, es un decorador. Si nosotros no pasamos alguno de los parámetros su valor por defecto sera None.

    - Getter: Se encargará de interceptar la lectura del atributo. (get = obtener)
    - Setter : Se encarga de interceptar cuando se escriba. (set = definir o escribir)
    - Deleter : Se encarga de interceptar cuando es borrado. (delete = borrar)
    - doc :  Recibirá una cadena para documentar el atributo. (doc = documentación)

Ejemplo practico:
'''

class Perros(object):                         #* Declaramos la clase principal Perros
    def __init__(self, nombre, peso):         #* Definimos los parámetros 
        self.__nombre = nombre                #* Declaramos los atributos (privados ocultos)
        self.__peso = peso

    @property                                 #* Este es el Getter
    def nombre(self):                         #* Definimos el método para obtener el nombre
        return self.__nombre                  #* Aca simplemente estamos retornando el atributo privado oculto

    '''
 - Hasta aquí definimos los métodos para obtener los atributos ocultos o privados getter.
 - Ahora vamos a utilizar setter y deleter para modificarlos
    '''

    @nombre.setter                                 #* Propiedad SETTER
    def nombre(self, nuevo):
        print ("Modificando nombre..")
        self.__nombre = nuevo
        print ("El nombre se ha modificado por")
        print (self.__nombre)                      #* Aquí vuelvo a pedir que retorne el atributo para confirmar

    @nombre.deleter                                #* Propiedad DELETER
    def nombre(self): 
        print("Borrando nombre..")
        del self.__nombre
    
    #* Hasta aquí property

    def peso(self):                                #* Definimos el método para obtener el peso
        return self.__peso                         #* Aquí simplemente estamos retornando el atributo privado

'''
Inicializamos el programa...
'''
Tomas = Perros('Tom', 27)
print (Tomas.nombre)                                #* Imprimimos el nombre de Tomas. Se hace a través de getter
                                                    #* Que en este caso como esta luego de property lo toma como el primer método..
Tomas.nombre = 'Tomasito'                           #* Cambiamos el atributo nombre que se hace a través de setter
del Tomas.nombre                                    #* Borramos el nombre utilizando deleter

#! En python todo esto es re contra re mil al pedo.