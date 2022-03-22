print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

            #Son como carpetas y sub carpetas (class padre y clas hijo), cada una con sus funciones dentro.
            #Siempre el nombre con la primera letra en mayuscula.
                                                 
class Animal:                                                                           #Clase padre.
    def __init__(self, nombre, onomatopeya):                                            #Funcion base o algo asi (instancia).
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):                                                                   #Funcion de saludo. El 'self.' es la variable local,
        print('Hola, soy un', self.tipo, 'y mi sonido es el', self.onomatopeya, "\n")   #se llama asi porque es un estandar.

class Gato(Animal):                                     #Funcion hijo.
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya):            #Esto anula la funcion base del padre, excepto que la nombre nuevamente.
        Animal.__init__(self, nombre, onomatopeya)      #Nombro nuevamente la funcion padre por su nombre (Animal).
        print('Hola, soy un gato extendido!')

class Perro(Animal):                                    #Funcion hijo.
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)           #Nombro nuevamente la funcion padre pero ahora con 'super' que hace referiencia a 'Animal'.
        print('instanciando un perro')

class Canario(Animal):                                  #Funcion hijo.
    tipo = 'canario'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('Soy un canario!!!')

gato = Gato('Fluffy', 'maullido')               #Asignacion a la funcion base.
gato.saludo()                                   #Llama a la funcion de saludo en la clase padre.

perro = Perro('Firulais', 'ladrido')
perro.saludo()

canario = Canario('Piolin', 'silvido')
canario.saludo()
  
print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")