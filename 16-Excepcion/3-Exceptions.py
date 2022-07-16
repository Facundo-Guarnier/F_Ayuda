class ErrorIgual(Exception):
    pass

class ErrorMayor(Exception):
    pass

class  ErrorTipoCuenta(Exception):
    pass


def funcion(a, b, c):
    if "suma" == c:
        try:
            return sumador(int(a), int(b)) 

        except ErrorIgual as e:
            print("ERROR 402: " + str(e))
            return 0

        except ErrorMayor as e:
            print("ERROR 403: " + str(e))
            return 0

        except ValueError as e:
            print("ERROR 100: No son numeors. \n" + str(e))
            return 0

        except Exception as e:
            print("ERROR 999: Error desconocido, comunicarse con el fabricante")
            print(e)
            return 0

    else:
        raise ErrorTipoCuenta("No es suma.")


def sumador(a,b):
    if a > b:
        raise ErrorMayor("A es mayor a B.")

    elif a == b:
        raise ErrorIgual("Son iguales.")
    
    else:
        return a + b



def funcion2(a):
    try: 
        if a == "Hola":
            raise Exception("Error es igual a Hola")
        else:
            return("11111111")
    except Exception as e:
        print(e)



if __name__ == "__main__":

    print("++++++++++++++++++++")           #Mando y recibo distintos errores entre clases y funciones
    try:
        print("El resultado es: " + str(funcion("5" , 5, "suma")))
    except ErrorTipoCuenta as e:
        print("ERROR: " + str(e))

    except Exception as e:
        print("ERROR 404: Error desconocido, comunicarse con el fabricante")
        print(e)
    print("++++++++++++++++++++")


    print("++++++++++++++++++++")           #En una misma funcion mando y recivo dentro del try
    print(funcion2("Holaa"))
    print("++++++++++++++++++++")
