import unittest

class ErrorEdad(Exception):
    pass


def edad(año):
    try:
        if 130 <= año:
            raise ErrorEdad("Estas grandecito")             #Envio una Error afuera de la funcion.
        return int(año)                                     #Envio y recivo en la misma funcion.
    except (ValueError, TypeError):
        print("Error: Es palabra")
        return 0
    

class TestTry(unittest.TestCase):
    def test_edad_mas_210(self):                        #Sale un error de la funcion por lo tanto uso assertRaises.
        with self.assertRaises(ErrorEdad):              #Para el programa hay un error de edad.
            edad(210)
    
    def test_edad_palabra(self):                        #Error dentro de la misma funcion, como no sale ningun error no puedo usar assertRaises
        self.assertEqual(edad("una palabra"), 0)        #Para el programa no hay ningun error.


if __name__ == '__main__':
    try:
        print(edad(500))
    except ErrorEdad as e:                      #Resivo el error que envie afuera de la funcion
        print("ERROR 4: " + str(e))
    unittest.main()
    

