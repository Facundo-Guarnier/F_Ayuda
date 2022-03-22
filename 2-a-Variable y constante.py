print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")
print ("---------------------------------------------------------------")
print ("------------------------Tipos/Type-----------------------------")
variable_1 = 1.123456789

variable_2, variable_3 = 1, 5       #Se puede definir 2 variable en una misma linea. 
print(variable_2 + variable_3)

entero = "int"                      #Números entero.
texto = "str"                       #Letras y números.
decimal = "float"                   #Números decimales (hay que utilizar el punto para el decimal).
valor_absoluto = "abs"              #Valor absoluto.
redondeo = "round(variable, x)"     #Redondeo los números. En x son los decimales que queres. 5.8 = 6, 9.5 = 9, 2.2 = 2
print(round(variable_1, 2))

variable = "AbCd"
print(variable.lower())         #Pasa toda la variable a minúscula
print(variable.upper())         #Pasa toda la variable a MAYÚSCULA.

print ("---------------------------------------------------------------")
print ("--------------------------Variable-----------------------------")   #Tiene un valor numérico o en letra.
                                                                            #Para renombrar la variable y todos sus llamados se usa "ctrl + F12".
                                                                            #Todo con minúscula y separado con guion bajo.

variable_1 = 8 + 5          #Una variable con una suma.
print(variable_1 + 100)     #Realiza una suma de la variable + 100
print(variable_1, 100)      #Une la variable con el 100 

variable_1 = 10
variable_2 = 5
variable_1, variable_2 = variable_2, variable_1     #Intercambiar valores de variables.
print(variable_1, variable_2)

print("----------------------------------------------------------------")
print("-------------------------Constante------------------------------")   #Una vez definida no se puede cambiar.
                                                                            #Se escribe todo con mayúsculas y guion bajo.

MI_CONSTANTE = 3.14159
print(MI_CONSTANTE)

print("\n+++++++++++++++++++++++++++++++++++++++ FIN ++++++++++++++++++++++++++++++++++++++++++++++++++\n")