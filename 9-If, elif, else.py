print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("---------------------------------------------------------------")
print("------------------- Condicional (if, else) --------------------")    #El código a ejecutar dentro de los condicionales tiene que estar con indentation.

la_condición = 15

if (la_condición > 15) and (la_condición < 100):                        #"si", si no cumple no hace nada.
     print("No deberia leer esto ya que no se cumple la condición1")

elif (1 < la_condición < 10):
     print("No deberia leer esto ya que no se cumple la condición2")

elif (la_condición == 15):                                            #Si el "si" anterior no se cumple pasa a este nuevo "si" ya que tiene condición.
     print("Es correcto")

else :                                                                #"Sino", cuando ningún "si" se cumplió, no tiene condición.
     print("No deberia leer esto ya que no se cumple la condición3")
     pass                                                             #Es para un Condicional cuando no se le asigna una acción y evitar error.


print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")