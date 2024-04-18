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
print("Sentencias condicionales compuestas (if-else): ")
print(" ")
#--------------------------------------------------------------
#NOTE - En Python, las sentencias condicionales compuestas,
#NOTE - Son aquellas que nos permiten tener instrucción a 
#NOTE - ejecutar de acuerdo a la condición establecida. 
#NOTE - Es decir, si la condición se cumple, habrá una
#NOTE - intrucción a ejecutar correspondiente a la rama
#NOTE - de verdadero.
#NOTE - De igual manera, si la condición no se cumple, habrá
#NOTE - otra instrucción a ejecutar correspondiente a la
#NOTE - rama de falso. 

#NOTE - En las sentencias condicionales compuestas, jamás
#NOTE - se ejecutarán de manera simultánea las instrucciones
#NOTE - de ambas, únicamente, se ejecutará la instrucción
#NOTE - correspondiente a la rama de verdadero o falso, cuya
#NOTE - decisión de determinada por la condición establecida. 
#--------------------------------------------------------------
"""  
                            INICIO
                              |
<-_____FALSO___________<-CONDICIÓN->_________VERDADERO____->
  |                                                        |
  |                                                        |
INTRUCCIÓN                                            INTRUCCIÓN  
  |                                                        |
  |___->_____________________________________________<-____|
                              |
                             FIN 
num_uno = 5
if num_uno == 5:
    print("El nro es cinco.")
else:
    print("El nro NO es cinco.")
    print(" ")
print ("Fin.")
"""
#--------------------------------------------------------------
print("Sistema para calcular el promedio de un alumno.")
print(" ")
nombre = input("Para comenzar, ¿cuál es tu nombre?: ")
apellido = input("Cuál es tu apellido?: ")
print(" ")
matematica = int(input(nombre + " ¿Cuál es tu calificación en matemáticas?: "))
quimica = int(input(nombre + "¿Cuál es tu nota de química?: "))
biologia = int(input(nombre +"¿Cuál es tu calificación en Biología?: "))

promedio = (matematica + quimica + biologia) / 3
print(" ")
if promedio >= 7 :
    print("¡Felicidades, ha aprobado! " + nombre + " " + apellido + "." + " Su promedio es: ", promedio)
else:
    print("El alumno no ha aprobado. Su promedio es: ", promedio)
print(" ")

