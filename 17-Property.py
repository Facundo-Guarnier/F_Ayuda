import unittest                             
from time import sleep                          
import datetime                                              

class ErrorFechaFuturo(Exception):
    pass

class  ErrorSueldoNegativo(Exception):
    pass

class ErrorProveedorCorreo(Exception):
    pass

class ErrorLargoNumero(Exception):
    pass


class Persona:
    def __init__(self, nombre="", apellido="", pais="", tel="", edad="", correo=""):
    
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad                                    
        self.correo = correo
        self.pais = pais
        self.tel = tel
        self.telefonos = ""
    
    def __str__(self):   
        return ("Apellido: " + self.__apellido + "\n" +
            "Nombre: " + self.__nombre + "\n" +
            "Telefono: "+ str(self.__telefonos) + "\n" +
            "Edad: " + str(self.__edad) + "\n" +
            "Pais: " + str(self.__pais) + "\n" +
            "Correo: " + str(self.__correo))
        


    def agregar_telefono(self, cod, tel):
        self.__telefonos.append(str(Telefono(cod, tel)))
        if "" in self.__telefonos:
            for i in range(self.__telefonos.count("")):
                self.__telefonos.remove("")
        

    @property
    def telefonos(self):
        return self.__telefonos
    
    @telefonos.setter
    def telefonos(self, value):
        self.__telefonos = [str(Telefono(self.__pais, self.__tel))]

    @property                               #Seria mi getter de un atributo (devuelve el valor)
    def nombre(self):                   
        return self.__nombre                #Este seria el nombre del atributo
    
    @nombre.setter                          #Seria mi setter, define el atributo y su valor
    def nombre(self, value):
        self.__nombre = value

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, value):
        self.__apellido = value
    
    @property
    def edad(self):
        return int(self.__edad) 

    @edad.setter                             
    def edad(self, value):
        try:
            self.__edad = int(value)
        except Exception as e:
            print("Valor erroneo.")
            self.__edad = "0"

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, value):
        try: 
            self.__correo = str(Email(value))
        except ErrorProveedorCorreo as e:
            print("ERROR 12: " + str(e))
            self.__correo = None
        except Exception as e: 
            print("ERROR 109: Error desconocido, comunicarse con el fabricante\n" + str(e))
            self.__correo = None
    
    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, value):
        if (value.upper()) == ("ARGENTINA") or (value.upper()) == "ARG":
            self.__pais = "Argentina"
        else:
            self.__pais = "Extranjero"

    @property
    def tel(self):
        return self.__tel

    @tel.setter
    def tel(self, value):
        self.__tel = value


class Email:
    def __init__(self, email=''):
        self.email = email
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        if not(("@gmail.com" in value) or ("@hotmail.com" in value)):
            self.__email = None
            raise ErrorProveedorCorreo("Proveedor (@) no es valido.")
        else:
            self.__email = value


    
    def __str__(self):
        return str(self.__email)
    

class Telefono:
    def __init__(self, cod_pais, numero):
        self.cod_pais = str(cod_pais)
        self.numero =  str(numero)
        

    @property
    def cod_pais(self):
        return self.__cod_pais

    @cod_pais.setter
    def cod_pais(self, value):
        if (value.upper()) == "ARGENTINA":
            self.__cod_pais = "+54 9 "
        else:
            self.__cod_pais = "<Internacional> "


    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, value):
        try:
            n_limpio = ""
            for i in value:
                if i != " ":
                    n_limpio += i
            if len(n_limpio) != 10:
                self.__numero = ""
                raise ErrorLargoNumero("No es un numero valido, longitud != 10.")
            try:
                n_limpio = int(n_limpio)
            except:
                print("ERROR 23: No se ingresó un numero.") 
                self.__numero = ""
                return

            n_limpio = list(str(n_limpio))
            n_limpio.insert(3, " ")
            n_limpio.insert(7, " ")
            n_limpio = "".join(n_limpio)
        
            self.__numero = n_limpio
            if "261" == self.__numero[:3]:
                self.__numero += " <Mendoza>"
        except ErrorLargoNumero as e: 
            print("ERROR 13: " + str(e))


        
    def __str__(self):
        if "" == self.__numero:
            return str(self.__numero)
        return str(self.__cod_pais + self.__numero)


class Empleado(Persona):

    def __init__(self, nombre="", apellido="", pais="", tel="", edad="", correo="", n_social="", sueldo=""):
        super().__init__(nombre, apellido,  pais, tel, edad, correo)
        self.__n_social = n_social
        self.__sueldo = sueldo

    @property
    def n_social(self):
        return self.__n_social

    @n_social.setter
    def n_social(self, value):
        self.__n_social = value

    @property
    def sueldo(self):
        return self.__sueldo

    @sueldo.setter
    def sueldo (self, value):
        try:
            if int(value) < 0:
                self.__sueldo = 0
                raise ErrorSueldoNegativo("Se ingresó un sueldo negativo.")
            else: 
                self.__sueldo = float(value)

        except ErrorSueldoNegativo as e:
            self.__sueldo = 0
            print("ERROR 12: " + str(e))
        except ValueError as e: 
            self.__sueldo = 0
            print("ERROR 40: No se ingreso un numero")
            print(e)
        except Exception as e: 
            self.__sueldo = 0
            print("ERROR 404: Error desconocido, comunicarse con el fabricante")
            print(e)



    def __str__(self):
        return (str(super().__str__()) + "\n" + 
            "N° Social: " + str(self.__n_social) + "\n" + 
            "Sueldo: " + str(self.__sueldo))


class Auto:
    def __init__(self, dueño="", modelo="", marca="", año=""):
        self.dueño = dueño
        self.modelo = modelo
        self.marca = marca
        self.año = año
        self.antiguedad = año
    
    
    def contar(self, año, hoy, n=0):
        n += 1 
        if  hoy == año:
            return n-1
        else:       
            return (self.contar(año + 1, hoy, n))


    @property
    def dueño(self):
        return self.__dueño

    @dueño.setter
    def dueño(self, value):
        self.__dueño = str(value)


    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, value):
        self.__modelo = value


    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, value):
        self.__marca = value

   
    @property
    def año(self):
        return self.__año

    @año.setter
    def año(self, value):
        self.__año = value


    @property
    def antiguedad(self):
        return self.__antiguedad

    
    @antiguedad.setter
    def antiguedad(self, value):
        hoy = datetime.date.today().year

        try:
            if hoy < value:
                self.__antiguedad = 0
                raise ErrorFechaFuturo("Ingreso una fecha en el futuro... .-.")
            else:
                self.__antiguedad = (self.contar(value, datetime.date.today().year))
        except ErrorFechaFuturo as e:
            self.__antiguedad = 0
            print("ERROr 705F: " + str(e))
        
        except TypeError as e: 
            self.__antiguedad = 0
            print("ERROR 404: No ingreso un año.")
        except Exception as e:
            self.__antiguedad = 0
            print("ERROR 404: Error desconocido, comunicarse con el fabricante")
            print(e)



    def __str__(self):
        return ("Marca: " + str(self.__marca) + "\n" + 
                "Modelo: " + str(self.__modelo) + "\n" + 
                "Año: "  + str(self.__año) + "\n" + 
                "Antiguedad: " + str(self.__antiguedad) + " años\n" +
                "Dueño: \n" + str(self.__dueño) + "\n")
                

class TestPersona(unittest.TestCase):
    #Telefonos
    def test_tel_no_valido(self):
            persona1 = Persona("Jose", "Perez", "Argentina", "261 555 320", "30", "@gmail.com")
            self.assertEqual(persona1.telefonos, [""])  

    def test_sin_telefono(self):
            persona1 = Persona("Jose", "Perez", edad="30", correo="@gmail.com")
            self.assertEqual(persona1.telefonos, [""]) 

    def test_agrega_tel_sin_telefono_desde_inicio(self):
            persona1 = Persona("Jose", "Perez", edad="30", correo="@gmail.com")
            persona1.agregar_telefono("Argentina", "2865558080")
            self.assertEqual(persona1.telefonos, ["+54 9 286 555 8080"]) 

    def test_2_telefonos(self):
            persona1 = Persona("Jose", "Perez", "Argentina", "265 555 3200", "30", "@gmail.com")
            persona1.agregar_telefono("Colombia", "2829995463")
            self.assertEqual(persona1.telefonos, ["+54 9 265 555 3200", "<Internacional> 282 999 5463"])

    def test_identificar_mendoza(self):
            persona1 = Persona("Jose", "Perez", "arg", "261 555 3200", "30", "@gmail.com")
            self.assertIn("<Mendoza>", str(persona1.telefonos))

    #Otros
    def test_persona1(self):
        persona1 = Persona("Jose", "Perez", "arg", "261 555 3200", "30", "@gmail.com")
        self.assertEqual(persona1.nombre, "Jose")
        self.assertEqual(persona1.apellido, "Perez")
        self.assertEqual(persona1.pais, "Argentina")
        self.assertEqual(persona1.telefonos, ['+54 9 261 555 3200 <Mendoza>'])
        self.assertEqual(persona1.edad, 30)
        self.assertEqual(persona1.correo, "@gmail.com") 

    def test_mal_edad(self):
        persona2 = Persona("Jose", "Perez", "arg", "261 555 3200", "treinta", "@gmail.com")
        self.assertEqual(persona2.nombre, "Jose")
        self.assertEqual(persona2.apellido, "Perez")
        self.assertEqual(persona2.pais, "Argentina")
        self.assertEqual(persona2.telefonos, ['+54 9 261 555 3200 <Mendoza>'])
        self.assertEqual(persona2.edad, 0)
        self.assertEqual(persona2.correo, "@gmail.com") 


class TestEmpleado(unittest.TestCase):
    #General
    def test_Empleado(self):
        empleado1 = Empleado("Facundo", "Guarnier", "Arg", "261 5117024", 18, "FG@gmail.com", 123456789, 55000)
        self.assertEqual(empleado1.nombre, "Facundo")
        self.assertEqual(empleado1.apellido, "Guarnier")
        self.assertEqual(empleado1.pais, "Argentina")
        self.assertEqual(empleado1.telefonos, ['+54 9 261 511 7024 <Mendoza>'])
        self.assertEqual(empleado1.correo, "FG@gmail.com") 
        self.assertEqual(empleado1.edad, 18)
        self.assertEqual(empleado1.n_social, 123456789)
        self.assertEqual(empleado1.sueldo, 55000)
        
    def test_mal_edad(self):
        empleado1 = Empleado("Facundo", "Guarnier", "Arg", "261 5117024", "8sa", "FG@gmail.com", 123456789, 55000)
        self.assertEqual(empleado1.edad, 0)

    #Telefono
    def test_tel_no_valido(self):
            empleado1 = Empleado("Facundo", "Guarnier", "Arg", "261 555 320", 18, "FG@gmail.com", 123456789, 55000)
            self.assertEqual(empleado1.telefonos, [""])  

    def test_sin_telefono(self):
            empleado1 = Empleado("Facundo", "Guarnier", "Arg", edad=18, correo="FG@gmail.com", n_social=123456789, sueldo=55000)
            self.assertEqual(empleado1.telefonos, [""]) 

    def test_agrega_tel_sin_telefono_desde_inicio(self):
            empleado1 = Empleado("Facundo", "Guarnier", "Arg", edad=18, correo="FG@gmail.com", n_social=123456789, sueldo=55000)
            empleado1.agregar_telefono("Argentina", "2865558080")
            self.assertEqual(empleado1.telefonos, ["+54 9 286 555 8080"]) 

    def test_2_telefonos(self):
            empleado1 = Empleado("Facundo", "Guarnier", "Arg", "265 555 3200", 18, "FG@gmail.com", 123456789, 55000)
            empleado1.agregar_telefono("Colombia", "2829995463")
            self.assertEqual(empleado1.telefonos, ["+54 9 265 555 3200", "<Internacional> 282 999 5463"])

    def test_identificar_mendoza(self):
            empleado1 = Empleado("Facundo", "Guarnier", "Arg", "261 555 3200", 18, "FG@gmail.com", 123456789, 55000)
            self.assertIn("<Mendoza>", str(empleado1.telefonos))


class TestTry(unittest.TestCase):
    def test_edad_numero_mal(self):
        empleado10 = Empleado("facu", "gua", "arg", 261555, "dos años", "fg", 4564456, 65)
        self.assertEqual(empleado10.edad, 0)
    
    def test_edad_numero_bien(self):
        empleado10 = Empleado("facu", "gua", "arg", 261555, 24, "fg", 4564456, 65)
        self.assertEqual(empleado10.edad, 24)
    
    def test_email_proveedor_mal(self):
        with self.assertRaises(ErrorProveedorCorreo):
            email1 = Email("facundo@gmail")
    
    def test_email_proveedor_bien(self):
        email1 = Email("facundo@gmail.com")
        self.assertEqual(email1.email, "facundo@gmail.com")
    


if __name__ == '__main__':
    """    
    print("--------Persona 1-------")
    #persona1 = Persona(input("Nombre: "), input("Apellido: "), input("Pais: "), input("Telefono: "), input("Edad: "), input("Correo: "))
    persona1 = persona2 = Persona("Jorge", "Guar", "ARGentina", "2615117024", "19", "@gmail.com")
    animation = "|/-\\"                                                                   #
    i = 10                                                                                #
    while i < 18:                                                                         #
        print("Guardando informacion...", animation[i % len(animation)], end="\r")        # Animacion de carga, from time import sleep
        i += 1                                                                            #
        sleep(0.5)                                                                        #
    print("------ \n")
    print("\n" + str(persona1))
    sleep(1.5) 
    print("------------------------\n \n")
    """


    print("--------Persona 2-------")
    persona2 = Persona("Facu", "Guar", "ARGentina", "2615117024", "19", "@gmail.com")
    persona2.agregar_telefono("argentina", "2616523939")
    print(persona2)
    print("------------------------\n \n")



    
    print("-------Empleado 1-------")
    empleado1 = Empleado("Facundo", "Guarnier", "Argentina", edad="63", correo="fag@gmañññññil.com", n_social="2144091597", sueldo=15200)
    empleado1.agregar_telefono("argentina", "261 562 3939")
    empleado1.agregar_telefono("argentina", "261 562 9")            #largo != 10
    empleado1.agregar_telefono("Colombia", "268 888 dddd")          #No es numero pero si el largo de 10


    print(empleado1)
    print("\n------\n")
    empleado1.sueldo = "dos pesos"                  #Error de palabra distinto a numero
    print(empleado1)
    print("------------------------\n \n")
    
    """
    print("-------Auto 1-------")
    auto1 = Auto(empleado1, "Astra", "Chevrolet", 2007)
    print(auto1)

    print("------------------------\n \n")
    """
    unittest.main()