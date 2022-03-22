print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("---------------------------------------------------------------")
print("---------------------While/Mientras que------------------------")

while True:                         #Esto genera un bucle infinito.
     print("Hola")    
     break                          #Esto termina el bucle completo, con los posibles else (sino:)
else:                               #Funciona igual que el else del if, también se usa para for
     print("Aca nunca llega por el break, ne deberías leer esto") 



variable_2 = 0

while variable_2 < 6: 
     variable_2 += 1
     if (variable_2 == 3):
          continue                  #Cuando el programa llega hasta Continue, este vuelve al inicio del programa sin hacer lo que hay debajo
                                    #Se utiliza con un "if" sino queda también en un bucle.
     print (variable_2)

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")