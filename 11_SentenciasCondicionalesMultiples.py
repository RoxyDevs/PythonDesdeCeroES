print(" ")
print("Python desde cero en Español")
print(" ")
#--------------------------------------------------------------
print("Author @RoxDev")
print(" ")
print ("Puedes apoyar mis proyectos en:")

base_url = "https://paypal.me/belakiss?country.x=AR&locale.x=es_XC"
print(base_url)
print(" ")
#--------------------------------------------------------------
print("Sentencias condicionales múltiples): ")
print(" ")
#--------------------------------------------------------------
#NOTE - En Python, al utilizar las sentencias condicionales
#NOTE - simples y compuestas, nos podemos encontrar con la
#NOTE - necesidad de integrar más de una condición, a una
#NOTE - misma estructura condicional.
#NOTE - Esta nos permite elegir una ruta de entre varias posibles,
#NOTE - con base al valor de una variable que actúa como selector.abs

#NOTE - En el momento en que alguna de las condiciones se cumpla,
#NOTE - se ejecuta la intrucción o instrucciones correspondientes
#NOTE - a dicha condición y la ejecución de la sentencia condicional
#NOTE - finalizará.

#* SINTAXIS:

#*  if Condición lógica:
#*        Instrucción
  
#* elif Condición lógica:
#*        Instrucción

#* else:
#*      Intrucción

"""
                                  INICIO
                                    |
                  (F)__________CONDICIÓN 1________(V)______->
                    |                                        |
                    |                                        |
                CONDICIÓN 2_____(V)                          |                 
                (F) |           |                       INSTRUCCIÓN 
  INSTRUCCIÓN_______|       INSTRUCCIÓN                      |
  |                             |                            |
  |____->_______________________|______________________<-____|
                                |
                              FIN 

num_uno= 1
if num_uno==1:
    print("El nro es UNO.")
elif num_uno==2:
    print("El nro es DOS.")
Else:
    print("El nro se desconoce.")
print("Fin.")
"""
print("=================================")
print("¡Convertidor de números a letras!")
print("=================================")
print(" ")
num_uno= int(input("¿Cuál es el nro que deseas convertir?: "))
if num_uno == 1:
    print("El nro es 'Uno'")
elif num_uno == 2:
    print("El nro es 'Dos'")
elif num_uno == 3:
    print("El nro es 'Tres'")
elif num_uno == 4:
    print("El nro es 'Cuatro'")
elif num_uno == 5:
    print("El nro es 'Cinco'")
else:
    print("Este programa solo puede convertir hasta el nro 5. ")
print("Fin.")
print(" ")
print("=================================")

